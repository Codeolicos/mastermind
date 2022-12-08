# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 12:16:24 2022

@author: Codeolicos
"""

import mm_gui_windows as mgw

def new_game_():
    """Command for the 'New game' button """
    print("new game")
    pass

def load_game_():
    """Command for the 'Continue' button """
    print("load game")
    pass

def about(MenuWindow):
    
    MenuWindow.closing_window()
    About = mgw.AboutWindow()
    About.mainloop()
    """Command for the 'About' button """
    print("about")
    pass