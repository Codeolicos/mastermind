# -*- coding: utf-8 -*-
"""
Created on Wed May 18 10:48:14 2022

@author: Codeolicos
"""

import mm_functions as mm_fun
import save_functions as save

class Start():
    """ 
    This class makes preparations for a new game
    
    Attributes
    ----------
    
    
    Methods
    -------
    
    """
    
    def __init__(self):
        """ """
        self.solution = mm_fun.generate_solution()
    
    
    