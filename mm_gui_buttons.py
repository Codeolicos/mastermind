# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:49:36 2022

@author: Codeolicos
"""

import tkinter as tk
import tkinter.ttk as ttk

class MainWindow (tk.Tk):
    
    def __init__(self):
        
        super().__init__()
        self.title("Mastermind")
        self.geometry("700x430")