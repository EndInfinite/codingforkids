#this is the initial work which includes a AI logic without any optimization
#this is done by xp

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from enum import Enum
import random


class TicTacToeBoard(tk.Frame):
    def __init__(self, master):
        super().__init__(master, background="darkslategray")
        self.master = master
        self.grid(row=0, column=0, sticky=tk.NSEW, padx=2, pady=2)
        self.cellMatrix = {}
        self.moveCount = 0

        #define 4 rows
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        #define 3 columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.firstPlayer = Player("X")  #always starts with first player, first player is alwasy a human
        self.secondPlayer = Player("O")  #second player can be a human or AI
        self.currentPlayerType = PlayerType.NoPlayer

        self.playMode = PlayMode.PlayerVsPlayer
        
        self.createWidges()
       
    
    def createWidges(self):
        #create a label for displaying PlayMode
        self.playModeLabel = ttk.Label(self, text=self.getDisplayNameforPlayMode())
        self.playModeLabel.grid(row=0, column=0, columnspan=3, sticky=tk.W+tk.E+tk.N)   #tk.W+tk.E will strech the label horizontally, tk.N will align the label to the top

        #create 9 buttons and assign them into 3x3 grid
        for i in range(3):
            for j in range(3):
                cell = ttk.Button(self, command=lambda x=i, y=j: self.button_clicked(x, y))
                cell.grid(row=i+1, column=j, padx=5, pady=5, sticky=tk.EW)
                self.cellMatrix[i,j] = cell

    #handle button click event, use x and y as the key to get the value (the clicked button) from cellMatrix dictionary
    def button_clicked(self, x, y):
        cell = self.cellMatrix[x, y]
        if cell["text"] != "":
            tk.messagebox.showwarning("Warning", "This move is not allowed.")
            return
        if self.playMode == PlayMode.PlayerVsPlayer:
            self.moveCount += 1
            playType = self.checkNextTurn()
            if playType == PlayerType.FirstPlayer:
                cell["text"] = self.firstPlayer.buttonIcon
                self.firstPlayer.setMove(x, y)
                if self.firstPlayer.checkIfWin():
                    tk.messagebox.showinfo("Win Result", "Player 1 won the game!")
                    self.restartGame()
                    return
                elif self.isGameDraw(): #check if the game is finished as draw, only need to check draw after first player's move
                    tk.messagebox.showinfo("Game Draw", "No winner, restart the game.")
                    self.restartGame()
                    return
            elif playType == PlayerType.SecondPlayer:
                cell["text"] = self.secondPlayer.buttonIcon
                self.secondPlayer.setMove(x, y)
                if self.secondPlayer.checkIfWin():
                    tk.messagebox.showinfo("Win Result", "Player 2 won the game!!!")
                    self.restartGame()
                    return
            else:   #this should not happen
                pass
            
        elif self.playMode == PlayMode.PlayerVsAI:
            #process human player's move
            self.moveCount += 1
            cell["text"] = self.firstPlayer.buttonIcon
            self.firstPlayer.setMove(x, y)
            if self.firstPlayer.checkIfWin():
                tk.messagebox.showinfo("Win Result", "Player 1 won the game!")
                self.restartGame()
                return
            elif self.isGameDraw():   #check if the game is finished as draw, only need to check draw after first player's move
                tk.messagebox.showinfo("Game Draw", "No winner, restart the game.")
                self.restartGame()
                return
            #let AI to pick up a move
            self.moveCount += 1
            self.AIMoveAsSecondPlayer()
        else:   #this should not happen
            pass

    def checkNextTurn(self):
        if self.currentPlayerType == PlayerType.NoPlayer:
            self.currentPlayerType = PlayerType.FirstPlayer
            return PlayerType.FirstPlayer   #this happens only when a game is initially started
        elif self.currentPlayerType == PlayerType.FirstPlayer:
            self.currentPlayerType = PlayerType.SecondPlayer
            return PlayerType.SecondPlayer
        elif self.currentPlayerType == PlayerType.SecondPlayer:
            self.currentPlayerType = PlayerType.FirstPlayer
            return PlayerType.FirstPlayer
        else:
            return PlayerType.NoPlayer  #return a default value, but this should not happen in all the cases

    def isGameDraw(self):
        if self.moveCount == 9:
            return True
        else:
            return False

    def restartGame(self):
        for i in range(3):
            for j in range(3):
                cell = self.cellMatrix[i, j]
                cell["text"] = ""
        self.firstPlayer.resetMoves()
        self.secondPlayer.resetMoves()
        self.currentPlayerType = PlayerType.NoPlayer
        self.moveCount = 0

    def setPlayMode(self, playMode):
        self.playMode = playMode
        self.playModeLabel["text"] = self.getDisplayNameforPlayMode()
        self.restartGame()
    
    def getDisplayNameforPlayMode(self):
        if self.playMode == PlayMode.PlayerVsPlayer:
            return "Player vs Player"
        elif self.playMode == PlayMode.PlayerVsAI:
            return "Player vs AI"
        else:
            return "Unknow Play Mode"

    def AIMoveAsSecondPlayer(self):
        #get the combined moves on the board
        combinedMoves = [[0]*3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                combinedMoves[i][j] = self.firstPlayer.moves[i][j] + self.secondPlayer.moves[i][j]

        #strategy: try all the possible winning moves first, then try the counter move to block human player, then get a random move
        #check the best winning move row by row
        for i in range(3):
            combinedRowSum = 0
            AIPlayerRowSum = 0
            AILastEmptyColumnIndex = 0
            for j in range(3):
                combinedRowSum += combinedMoves[i][j]
                AIPlayerRowSum += self.secondPlayer.moves[i][j]
                if self.secondPlayer.moves[i][j] == 0:   #AI player did not occupy this column
                    AILastEmptyColumnIndex = j
            if combinedRowSum == 2: #there is an empty cell in this row
                if AIPlayerRowSum == 2: #AI already occuplied 2 cells in this row, now AI has the chance to win, so seize it
                    #get the cell where the AI player did not occupy
                    cell = self.cellMatrix[i, AILastEmptyColumnIndex] 
                    cell["text"] = self.secondPlayer.buttonIcon
                    self.secondPlayer.setMove(i, AILastEmptyColumnIndex)
                    if self.secondPlayer.checkIfWin():
                        tk.messagebox.showinfo("Win Result", "AI won the game!")
                        self.restartGame()
                    return
            else:   
                continue
            
        #check the best winning move column by column
        for i in range(3):
            combinedColumnSum = 0
            AIPlayerColumnSum = 0
            AILastEmptyRowIndex = 0
            for j in range(3):
                combinedColumnSum += combinedMoves[j][i]
                AIPlayerColumnSum += self.secondPlayer.moves[j][i]
                if self.secondPlayer.moves[j][i] == 0:   #AI player did not occupy this row
                    AILastEmptyRowIndex = j
            if combinedColumnSum == 2: #there is an empty cell in this column
                if AIPlayerColumnSum == 2:  #AI player already occupied 2 cells in this column, now AI has the chance to win, so seize it
                    #get the cell where the AI player did not occupy
                    cell = self.cellMatrix[AILastEmptyRowIndex, i] 
                    cell["text"] = self.secondPlayer.buttonIcon
                    self.secondPlayer.setMove(AILastEmptyRowIndex, i)
                    if self.secondPlayer.checkIfWin():
                        tk.messagebox.showinfo("Win Result", "AI won the game!")
                        self.restartGame()
                    return
            else:   
                continue
        
        #check the best winning move for the first diagonal line
        combinedDiagonalSum = combinedMoves[0][0] + combinedMoves[1][1] + combinedMoves[2][2]
        AIPlayerDiagonalSum = self.secondPlayer.moves[0][0] + self.secondPlayer.moves[1][1] + self.secondPlayer.moves[2][2]
        if combinedDiagonalSum == 2:    #there is an empty cell in this diagonal
            if AIPlayerDiagonalSum == 2: #AI player already occupied 2 cells in this diagonal, now AI has the chance to win, so seize it
                AILastEmptyCellIndex = 0
                for i in range(3):
                    if self.secondPlayer.moves[i][i] == 0:
                        AILastEmptyCellIndex = i
                #get the cell of the diagonal where the AI player did not occupy
                cell = self.cellMatrix[AILastEmptyCellIndex, AILastEmptyCellIndex] 
                cell["text"] = self.secondPlayer.buttonIcon
                self.secondPlayer.setMove(AILastEmptyCellIndex, AILastEmptyCellIndex)
                if self.secondPlayer.checkIfWin():
                    tk.messagebox.showinfo("Win Result", "AI won the game!")
                    self.restartGame()
                return     
        
        #check the best winning move for the second diagonal line
        combinedDiagonalSum = combinedMoves[2][0] + combinedMoves[1][1] + combinedMoves[0][2]
        AIPlayerDiagonalSum = self.secondPlayer.moves[2][0] + self.secondPlayer.moves[1][1] + self.secondPlayer.moves[0][2]
        if combinedDiagonalSum == 2:    #there is an empty cell in this diagonal
            if AIPlayerDiagonalSum == 2: #AI player already occupied 2 cells in this diagonal, now AI has the chance to win, so seize it
                AILastEmptyRowIndex = 0
                AILastEmptyColumnIndex = 0
                if self.secondPlayer.moves[2][0] == 0:
                    AILastEmptyRowIndex = 2
                    AILastEmptyColumnIndex = 0
                if self.secondPlayer.moves[1][1] == 0:
                    AILastEmptyRowIndex = 1
                    AILastEmptyColumnIndex = 1
                if self.secondPlayer.moves[0][2] == 0:
                    AILastEmptyRowIndex = 0
                    AILastEmptyColumnIndex = 2
                #get the cell of the diagonal where the AI player did not occupy
                cell = self.cellMatrix[AILastEmptyRowIndex, AILastEmptyColumnIndex] 
                cell["text"] = self.secondPlayer.buttonIcon
                self.secondPlayer.setMove(AILastEmptyRowIndex, AILastEmptyColumnIndex)
                if self.secondPlayer.checkIfWin():
                    tk.messagebox.showinfo("Win Result", "AI won the game!")
                    self.restartGame()
                return  

        #check the best counter move row by row
        for i in range(3):
            combinedRowSum = 0
            humanPlayerRowSum = 0
            humanLastEmptyColumnIndex = 0
            for j in range(3):
                combinedRowSum += combinedMoves[i][j]
                humanPlayerRowSum += self.firstPlayer.moves[i][j]
                if self.firstPlayer.moves[i][j] == 0:   #human player did not occupy this column
                    humanLastEmptyColumnIndex = j
            if combinedRowSum == 2: #there is an empty cell in this row
                if humanPlayerRowSum == 2:  #human player already occupied 2 cells in this row, AI has to block it
                    #get the cell where the humn player did not occupy
                    cell = self.cellMatrix[i, humanLastEmptyColumnIndex] 
                    cell["text"] = self.secondPlayer.buttonIcon
                    self.secondPlayer.setMove(i, humanLastEmptyColumnIndex)
                    if self.secondPlayer.checkIfWin():
                        tk.messagebox.showinfo("Win Result", "AI won the game!")
                        self.restartGame()
                    return
            else:   
                continue        
    
        #check the best counter move column by column
        for i in range(3):
            combinedColumnSum = 0
            humanPlayerColumnSum = 0
            humanLastEmptyRowIndex = 0
            for j in range(3):
                combinedColumnSum += combinedMoves[j][i]
                humanPlayerColumnSum += self.firstPlayer.moves[j][i]
                if self.firstPlayer.moves[j][i] == 0:   #human player did not occupy this row
                    humanLastEmptyRowIndex = j
            if combinedColumnSum == 2: #there is an empty cell in this column
                if humanPlayerColumnSum == 2:  #human player already occupied 2 cells in this column, AI has to block it
                    #get the cell where the humn player did not occupy
                    cell = self.cellMatrix[humanLastEmptyRowIndex, i] 
                    cell["text"] = self.secondPlayer.buttonIcon
                    self.secondPlayer.setMove(humanLastEmptyRowIndex, i)
                    if self.secondPlayer.checkIfWin():
                        tk.messagebox.showinfo("Win Result", "AI won the game!")
                        self.restartGame()
                    return
            else:   
                continue

        
        
        #check the best counter move for the first diagonal line
        combinedDiagonalSum = combinedMoves[0][0] + combinedMoves[1][1] + combinedMoves[2][2]
        humanPlayerDiagonalSum = self.firstPlayer.moves[0][0] + self.firstPlayer.moves[1][1] + self.firstPlayer.moves[2][2]
        if combinedDiagonalSum == 2:    #there is an empty cell in this diagonal
            if humanPlayerDiagonalSum == 2: #human player already occupied 2 cells in this diagonal, AI has to block it
                humanLastEmptyCellIndex = 0
                for i in range(3):
                    if self.firstPlayer.moves[i][i] == 0:
                        humanLastEmptyCellIndex = i
                #get the cell of the diagonal where the humn player did not occupy
                cell = self.cellMatrix[humanLastEmptyCellIndex, humanLastEmptyCellIndex] 
                cell["text"] = self.secondPlayer.buttonIcon
                self.secondPlayer.setMove(humanLastEmptyCellIndex, humanLastEmptyCellIndex)
                if self.secondPlayer.checkIfWin():
                    tk.messagebox.showinfo("Win Result", "AI won the game!")
                    self.restartGame()
                return
                
        #check the best counter move for the second diagonal line
        combinedDiagonalSum = combinedMoves[2][0] + combinedMoves[1][1] + combinedMoves[0][2]
        humanPlayerDiagonalSum = self.firstPlayer.moves[2][0] + self.firstPlayer.moves[1][1] + self.firstPlayer.moves[0][2]
        if combinedDiagonalSum == 2:    #there is an empty cell in this diagonal
            if humanPlayerDiagonalSum == 2: #human player already occupied 2 cells in this diagonal, AI has to block it
                humanLastEmptyRowIndex = 0
                humanLastEmptyColumnIndex = 0
                if self.firstPlayer.moves[2][0] == 0:
                    humanLastEmptyRowIndex = 2
                    humanLastEmptyColumnIndex = 0
                if self.firstPlayer.moves[1][1] == 0:
                    humanLastEmptyRowIndex = 1
                    humanLastEmptyColumnIndex = 1
                if self.firstPlayer.moves[0][2] == 0:
                    humanLastEmptyRowIndex = 0
                    humanLastEmptyColumnIndex = 2
                #get the cell of the diagonal where the humn player did not occupy
                cell = self.cellMatrix[humanLastEmptyRowIndex, humanLastEmptyColumnIndex] 
                cell["text"] = self.secondPlayer.buttonIcon
                self.secondPlayer.setMove(humanLastEmptyRowIndex, humanLastEmptyColumnIndex)
                if self.secondPlayer.checkIfWin():
                    tk.messagebox.showinfo("Win Result", "AI won the game!")
                    self.restartGame()
                return  
        
        
        #as there is no best move found, select a random move from the empty cells in the board
        while True:
                x = random.randrange(0, 3)      
                y = random.randrange(0, 3)
                if combinedMoves[x][y] == 0:    #this cell is empty
                    cell = self.cellMatrix[x, y] 
                    cell["text"] = self.secondPlayer.buttonIcon
                    self.secondPlayer.setMove(x, y)
                    if self.secondPlayer.checkIfWin():
                        tk.messagebox.showinfo("Win Result", "AI won the game!")
                        self.restartGame()
                    return    

class Player:
    def __init__(self, buttonIcon):
        self.buttonIcon = buttonIcon
        self.moves = [[0]*3 for i in range(3)]  #set the initial move to 0 for a 3x3 matrix which means no cell is selected by the player
        
    def setMove(self, i, j):
        self.moves[i][j] = 1

    def checkIfWin(self):
        #check each row if all the cells are selected by the same player
        for i in range(3):
            rowSum = 0
            for j in range(3):
                rowSum += self.moves[i][j]
            if rowSum == 3:
                return True
        #check each colum if all the cells are selected by the same player
        for i in range(3):
            columnSum = 0
            for j in range(3):
                columnSum += self.moves[j][i]
            if columnSum == 3:
                return True
        #check diagonal direction if all the cells are selected by the same player
        diagonalSum = self.moves[0][0] + self.moves[1][1] + self.moves[2][2]
        if diagonalSum == 3:
            return True
        diagonalSum = self.moves[2][0] + self.moves[1][1] + self.moves[0][2]
        if diagonalSum == 3:
            return True

    def resetMoves(self):
        for i in range(3):
            for j in range(3):
                self.moves[i][j] = 0

class PlayerType(Enum):
    NoPlayer = 0
    FirstPlayer = 1
    SecondPlayer = 2

class PlayMode(Enum):
    PlayerVsPlayer = 1
    PlayerVsAI = 2


root = tk.Tk()
root.geometry("300x150")
root.title("Tic Tac Toe")
root.config(background = "orange")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

board = TicTacToeBoard(root)

#create the root menu bar
menuBar = tk.Menu(root)

#create "File" sub menu
fileMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Restart Game", command=lambda: board.restartGame())
fileMenu.add_command(label="Quit", command=root.quit)

#create "Play Mode" sub menu
playModeMenu = tk.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Play Mode", menu=playModeMenu)
playModeMenu.add_command(label="Player vs Player", command=lambda: board.setPlayMode(PlayMode.PlayerVsPlayer))
playModeMenu.add_command(label="Player vs AI", command=lambda: board.setPlayMode(PlayMode.PlayerVsAI))


# display the root menu bar
root.config(menu=menuBar)

root.mainloop()
