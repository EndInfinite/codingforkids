import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

class MyFrame1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background = "blue", borderwidth=1, padx = 2, pady = 5)
        self.master = master
        #self.pack(side = tk.TOP, fill = tk.X)   #fill the entire area of root window
        self.grid(row = 0, column = 1, sticky = tk.EW)
        self.createWidges()

    def createWidges(self):
        button1 = ttk.Button(self, text="Button 1")
        button1.pack(side = tk.LEFT, padx = 10)
        button1["command"] = self.button1_clicked
        
        button2 = ttk.Button(self, text="Button 2")
        button2.pack(side = tk.LEFT)
        
    def button1_clicked(self):
        message = tk.messagebox.askyesno("Hello", "Are you lucky today?")
        print("are your feeling lucky today?", message)


class MyFrame2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background = "yellow", borderwidth = 1, padx = 2, pady = 5)
        self.master = master
        #self.pack(side = tk.BOTTOM, fill = tk.X)   #fill the entire area of root window
        self.grid(row = 1, column = 0, sticky = tk.EW)

        #define a grid within the area of this frame
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)
        

        self.createWidges()

    def createWidges(self):
        button1 = ttk.Button(self, text="Button 1", command = lambda: self.button1_clicked("Happy XP"))
        button1.grid(row = 0, column = 0, sticky = tk.EW)
        
        
        button2 = ttk.Button(self, text="Button 2")
        button2.grid(row = 1, column = 1, sticky = tk.EW)

    def button1_clicked(self, buttonText):
        message = tk.messagebox.askyesno(buttonText, "Are you happy today?")
        print("are your feeling happy today?", message)

class MyFrame3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, background = "green", borderwidth = 1, padx = 2, pady = 5)
        self.master = master
        #self.pack(side = tk.BOTTOM, fill = tk.X)   #fill the entire area of root window
        self.grid(row = 2, column = 0, columnspan = 2, sticky = tk.EW)

        #define a grid within the area of this frame
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)

        self.createWidges()

    def createWidges(self):
        label1 = ttk.Label(self, text="Your name")
        label1.grid(row = 0, column = 0, sticky = tk.E, padx = 5)
        
        entry1 = ttk.Entry(self)
        entry1.grid(row = 0, column = 1, sticky = tk.EW)
        
        
        button1 = ttk.Button(self, text="Show your name", command = lambda: self.button1_clicked(entry1.get()))
        button1.grid(row = 1, column = 0, columnspan = 2, sticky = tk.EW, padx = 2, pady = 5)

    def button1_clicked(self, entryText):
        message = tk.messagebox.showinfo("Show Name", "Hello " + entryText + "!")
        
root = tk.Tk()
root.title("My Simply Window")
root.geometry("300x200")

root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)

root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)


MyFrame1(root)
MyFrame2(root)
MyFrame3(root)

root.mainloop()