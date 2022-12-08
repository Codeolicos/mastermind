import tkinter as tk
import tkinter.ttk as ttk

import mm_gui_functions_file as mm_guff
import mm_gui_classes as mmg
import mm_answer_imitation as mm_ai
from protocontroller import GameState
import mm_functions as mm_fun




class CombinationDisplay(ttk.Frame):
    """ """
    
    def __init__(self, master, combination):
        """ """
        
        super().__init__()
        
        self.master = master
        self.combination = combination
        
        for i in range(1, 5):
            lbl = tk.Label(master, text="     ", bg=combination[i])
            lbl.pack(side=tk.LEFT)
            space = tk.Label(master, text=" ", bg="white")
            space.pack(side=tk.LEFT)
            
        self.pack()

        

class AnswerDisplay(ttk.LabelFrame):
    """ """
    
    def __init__(self, iteration, answer, text):
        
        super().__init__(text)
        self.iteration = iteration
        self.answer = answer
        
        self.text("Try №{}".format(iteration))
        self.position = CombinationDisplay(self, answer["position"])
        self.reply = CombinationDisplay(self, answer["reply"])
        self.pack()

w = tk.Tk()
w.title("probe")
w.geometry("200x200")

g = GameState()


def press():
    guess = mm_ai.answer_imitation()
    iteration = g.iteration
    LF = AnswerDisplay(iteration, guess)
    
    
button = ttk.Button(w, text="press", command=press)
button.pack()






















w.mainloop()