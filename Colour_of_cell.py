# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 15:45:29 2022

@author: Codeolicos
"""

import tkinter as tk
import tkinter.ttk as ttk

w = tk.Tk()

class ColourOfCell(ttk.Frame):
    """ """
    
    colours = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]
    
    def __init__(self):
        
        super().__init__()
        current_colour = tk.StringVar()
        current_colour.set(self.colours[0])
        cell = tk.Label(text="  ", bg="{}".format(current_colour))
        cell.pack(side=tk.LEFT)
        
        for colour in self.colours:
            colour_rad = ttk.Radiobutton(text="", command=self.paint, 
                                         bg="{}".format(colour))
            colour_rad.pack(side=tk.LEFT)
                       
    def paint(self):
        pass
        
one = ColourOfCell()
one.pack()

w.mainloop()