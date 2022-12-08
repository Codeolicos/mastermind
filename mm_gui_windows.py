# -*- coding: utf-8 -*-
"""
Created on Sun Aug  7 18:29:07 2022

@author: Codeolicos
"""

import tkinter as tk
import tkinter.ttk as ttk
import Menu_window_controller as mwc


class BasicWindow(tk.Tk):
    """ This window is the base for almost any window in the game 
        This class is perfectly working"""
    
    def __init__(self):
        """ """
        
        super().__init__()
        self.title("Mastermind")
        self.geometry("700x430")
        self.protocol("WM_DELETE_WINDOW", self.game_exit)
        self.resizable(False, False)
    
    
    def game_exit(self):
        """ Creates a small window, which asks a player, does player
            want to quit and closes game, if confirmed"""
            
        endspiel = QuitWindow(self)
        endspiel.mainloop()
    
    def switch_windows(self, AnotherWindow):
        """Closes this window and opens some other window.
        
           Arguments:
               self : class 
               AnotherWindow : class
               
           Both classes are windowes, based on BasicWindow class
        """
        
        self.destroy()
        new_window = AnotherWindow
        new_window.mainloop()
        
        
        
class QuitWindow(tk.Tk):
    
    """Disables a game window, then creates a small window to clarify 
    player's decision to exit the game. If canceled, enables window.
    This class is perfectly working"""
    
    def __init__(self, victim_window):
        """"""
        
        super().__init__()
        self.geometry("200x60")
        self.resizable(False, False)
        self.title("Quit")
        self.victim_window = victim_window
        
        
        question_label = ttk.Label(self, 
                                   text="Are you sure you want to quit?")
        question_label.place(x=10, y=0)
        
        yes_button = ttk.Button(self, text="Yes", 
                        command=lambda : self._confirm_exit(victim_window))
        yes_button.place(x=10, y=30)
        
        no_button = ttk.Button(self, text="No", 
                        command= lambda : self._cancel_exit(victim_window))
        no_button.place(x=100, y=30)
        victim_window.attributes("-disabled", True)
        self.protocol("WM_DELETE_WINDOW", 
                      lambda : self._cancel_exit(victim_window))
        
        
    def _confirm_exit(self, victim_window):
        """ Just closes everything """
        self.victim_window.destroy()
        self.destroy()
        
    
    def _cancel_exit(self, victim_window):
        """ Enables the game window, then closes exit window """
        self.victim_window.attributes("-disabled", False)
        self.destroy()

class MenuWindow(BasicWindow):
    """ 
        Seems to work"""
    def __init__(self):
        """ """
        
        super().__init__()
        self._menu_buttons()
        
    def _menu_buttons(self):
        """ Creates and places menu buttons"""
        
        new_game_button = ttk.Button(self, text="New game", 
                                     command=mwc.new_game_)
        load_game_button = ttk.Button(self, text="Continue", 
                                      command=mwc.load_game_)
        about_button = ttk.Button(self, text="About", 
                command=lambda : self.switch_windows(AboutWindow()))
        exit_button = ttk.Button(self, text="Exit", command=self.game_exit)
        
        new_game_button.place(x=255 ,y=120 , width=200, heigh=50)
        load_game_button.place(x=255 ,y=170 , width=200, heigh=50)
        about_button.place(x=255 ,y=220 , width=200, heigh=50)
        exit_button.place(x=255, y=270, width=200, heigh=50)

class AboutWindow(BasicWindow):
    """A window with information about the game and the link to my git 
       repository"""
       
    def __init__(self):
        super().__init__()
    
        back_to_menu = ttk.Button(self, text="Back to menu", 
                    command=lambda : self.switch_windows(MenuWindow()))
        back_to_menu.place(x=0, y=0)
        
class GameWindow(BasicWindow):
    """ """
    def __init__(self):
        """ """
        
        super().__init__()
        self.columnconfigure(0, weight=1)
        
    