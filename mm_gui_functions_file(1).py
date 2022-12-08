# -*- coding: utf-8 -*-
"""
Created on Sat May 14 11:28:59 2022

@author: Codeolicos
"""

import tkinter as tk
import tkinter.ttk as ttk

import mm_answer_imitation as mm_ai

window = tk.Tk()
window.title("Output test")
window.geometry("700x430")

guesses_frame = ttk.LabelFrame(window, text="Guesses")
guesses_frame.pack(side=tk.RIGHT)



def colour_display(result):
    
    
    display_frame = ttk.LabelFrame(guesses_frame, 
                                   text="Try №{}".format(iteration))
    
    position_frame = ttk.Frame(display_frame)
    reply_frame = ttk.Frame(display_frame)
    
    # Display frame displays information about combination player
    # tried this turn (position) and combination with hints about
    # matches with original combination (reply).
    
   
    
    
    for i in range(1, 5):
        lbl = tk.Label(position_frame, text = "     ",
                        bg=result["position"][i])
        lbl.pack(side=tk.LEFT)
        space = tk.Label(position_frame, text=" ",
                         bg="white")
        space.pack(side=tk.LEFT)
        
    for i in range(1, 5):
        lbl = tk.Label(reply_frame, text = "     ",
                        bg=result["reply"][i])
        lbl.pack(side=tk.LEFT)
        space = tk.Label(reply_frame, text=" ",
                         bg="white")
        space.pack(side=tk.LEFT)
        
    position_frame.pack(side=tk.LEFT)
    reply_frame.pack(side=tk.RIGHT)
    
    display_frame.pack()
    
def packing_frame(result):
    display_frame = colour_display(result)
    display_frame.pack()
    
def sorcery():
    result = mm_ai.answer_imitation()
    colour_display(result)
    
result = mm_ai.answer_imitation()
btn = tk.Button(window, text="Press", 
                command=sorcery)
btn.pack()




# window.mainloop()
    