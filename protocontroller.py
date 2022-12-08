# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:39:55 2022

@author: Codeolicos
"""
import mm_functions as mm_fun
import save_functions as mm_save_fun

class GameState():
    """This class contains information about game statement"""
    
    def __init__(self):
        """"""
        self.iteration = 0
        self.remaining_attempts = 10 - self.iteration
        
        
    def recieve_iteration(self):
        """ 
        Arguments:
        
        Returns:
        
        """
        return self.iteration
    
    def start(self):
        """ """
        
        
        mm_save_fun.cleaning_save_file()
        cipher = mm_save_fun.encrypt_solution(self.solution)
        mm_save_fun.recording_cipher(cipher)
        
    
    
# g = GameState()
# a = g.recieve_number()
# b = g.recieve_number()
# c = g.recieve_number()
# print(a, b, c)
