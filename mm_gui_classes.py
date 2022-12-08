# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:48:14 2022

@author: Codeolicos
"""

import tkinter as tk
import tkinter.ttk as ttk

import mm_answer_imitation as mm_ai

class AllGuesses(tk.LabelFrame):
    """ """
    def __init__(self, master):
        """ """
        
        super().__init__(master, text="Guesses")
        self.master = master



class AttemptFrame(tk.LabelFrame):
    """ """
    def __init__(self, attempt):
        """This class   """
        
        self.iteration = NewGame.iteration
        super().__init__(master=AllGuesses, 
            text="Attempt №{}".format(self.iteration))
        
        self.attempt = attempt
        
    def display_attempt(self):
        """ 
        
        Arguments:
        
        Returns:
        
        """
        
        position = mmg.CombinationDisplay(self, 
                                          self.attempt['position'])
        reply = mmg.CombinationDisplay(self, self.attempt['reply'])
        position.grid(row=0, column=0)
        reply.grid(row=0, column=1)
        self.grid(column=0, row=self.iteration)
        
        

        
class CombinationDisplay(ttk.Frame):
    """ """
    
    def __init__(self, master, combination):
        """ """
        
        super().__init__()
        
        self.master = master
        self.combination = combination
        
        space = tk.Label(master, text=" ", bg="white")
        space.pack(side=tk.LEFT)
            
        for i in range(1, 5):
            lbl = tk.Label(master, text="     ", 
                           bg=combination[i])
            lbl.pack(side=tk.LEFT)
            space = tk.Label(master, text=" ", bg="white")
            space.pack(side=tk.LEFT)
            
        
        

