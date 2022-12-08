# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:48:14 2022

@author: Codeolicos
"""

import tkinter as tk
import tkinter.ttk as ttk


import mm_gui_windows as wind
import mm_functions as mm_fun
import mm_gui_classes as mmg
from protocontroller import GameState
from mm_answer_imitation import answer_imitation


w = wind.GameWindow()
NewGame = GameState()


class AllGuesses(tk.LabelFrame):
    """ """
    def __init__(self, master):
        """ """
        
        super().__init__(master, text="Guesses")
        self.master = master
        
        
    

class AttemptFrame(tk.LabelFrame):
    """ """
    def __init__(self, attempt):
        """ """
        
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
        
        
       
AllGuesses = AllGuesses(w)
AllGuesses.grid(row=0, column=1)
    



def sorcery():
    """ """

    NewGame.iteration += 1
    attempt = answer_imitation()
    
    new_try = AttemptFrame(attempt)
    new_try.display_attempt()

    
sorc_btn = ttk.Button(w, text="Sorcery", command=sorcery)
sorc_btn.grid(row=0, column=0, sticky="nw")


w.mainloop()
