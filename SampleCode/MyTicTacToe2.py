#this is the second version which optimized the AI logic

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from enum import Enum
import random
import copy


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

        #create a style for a font
        s = ttk.Style()
        #TButton is the default stype of ttk.Button, when creating a new stype for button, the style name format should be "newName.defaultName"
        s.configure("my.TButton", font=("Helvetica", 16))   

        #create 9 buttons and assign them into 3x3 grid
        for i in range(3):
            for j in range(3):
                cell = ttk.Button(self, style="my.TButton", command=lambda x=i, y=j: self.button_clicked(x, y))
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
                if self.checkIfWin(self.firstPlayer.moves):
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
                if self.checkIfWin(self.secondPlayer.moves):
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
            if self.checkIfWin(self.firstPlayer.moves):
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

    def checkIfWin(self, moves):
        #check each row if all the cells are selected by the same player
        for i in range(3):
            rowSum = 0
            for j in range(3):
                rowSum += moves[i][j]
            if rowSum == 3:
                return True
        #check each colum if all the cells are selected by the same player
        for i in range(3):
            columnSum = 0
            for j in range(3):
                columnSum += moves[j][i]
            if columnSum == 3:
                return True
        #check diagonal direction if all the cells are selected by the same player
        diagonalSum = moves[0][0] + moves[1][1] + moves[2][2]
        if diagonalSum == 3:
            return True
        diagonalSum = moves[2][0] + moves[1][1] + moves[0][2]
        if diagonalSum == 3:
            return True

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
        #check the best winning move for AI (try each empty cell on the board to see if AI can win if moving to this cell)
        for i in range(3):
            for j in range(3):
                if combinedMoves[i][j] == 0:    #empty cell on the board
                    tempMovesForAIPlayer = copy.deepcopy(self.secondPlayer.moves)    # copy the existing list to a new list
                    tempMovesForAIPlayer[i][j] = 1  #assume AI will occupy this cell, then check if AI can win
                    if self.checkIfWin(tempMovesForAIPlayer):
                        #get the cell where the AI player is going to occupy in order to win the game
                        cell = self.cellMatrix[i, j] 
                        cell["text"] = self.secondPlayer.buttonIcon
                        self.secondPlayer.setMove(i, j)
                        tk.messagebox.showinfo("Win Result", "AI won the game!")
                        self.restartGame()
                        return
        
        #check the best counter move for AI to block human from winning
        for i in range(3):
            for j in range(3):
                if combinedMoves[i][j] == 0:    #empty cell on the board
                    tempMovesForHumanPlayer = copy.deepcopy(self.firstPlayer.moves)    #copy the existing list to a new list
                    tempMovesForHumanPlayer[i][j] = 1  #assume human will occupy this cell, then check if human can win
                    if self.checkIfWin(tempMovesForHumanPlayer):    #if human can win the game by occupying this cell, AI must occupy it first in order to block human from winning
                        #get the cell where the AI player is going to occupy in order to block human from winning the game
                        cell = self.cellMatrix[i, j] 
                        cell["text"] = self.secondPlayer.buttonIcon
                        self.secondPlayer.setMove(i, j)
                        if self.checkIfWin(self.secondPlayer.moves):
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
                    if self.checkIfWin(self.secondPlayer.moves):
                        tk.messagebox.showinfo("Win Result", "AI won the game!")
                        self.restartGame()
                    return    

class Player:
    def __init__(self, buttonIcon):
        self.buttonIcon = buttonIcon
        self.moves = [[0]*3 for i in range(3)]  #set the initial move to 0 for a 3x3 matrix which means no cell is selected by the player
        
    def setMove(self, i, j):
        self.moves[i][j] = 1

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
