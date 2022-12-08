# -*- coding: utf-8 -*-
"""
Created on Tue May  3 12:29:20 2022

@author: Codeolicos
"""

import tkinter as tk
from tkinter import ttk

# main_window = Tk()
# main_window.title("Mastermind")
# main_window.geometry("640x480")

# main_window.mainloop()

game_screen = tk.Tk()
game_screen.title("Mastermind")
game_screen.geometry("640x480")

# cell_ = ttk.Combobox(game_screen, width=10)
# cell_["values"] = (" ", " ", " ", " ")
# cell_.place(x=, y=)

cell_ = ttk.Combobox(game_screen, width=2)
cell_["values"] = (" ", " ", " ", " ")
cell_.place(x=50, y=50)

b = tk.Button(game_screen, text="test", command=None, bg="cyan")
b.pack()
game_screen.mainloop()