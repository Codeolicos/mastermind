# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:19:48 2022

@author: Codeolicos
"""

import mm_functions as mm_fun
import save_functions as save

class Load():
    """ 
    This class takes and holds information from the save file. 
    
    Attributes
    ----------
    _records : list
        All records from the save file.
    iteration : int
        Number of turns the player has made.
    solution : dict
        Decrypted and restored combination of colours the player has to 
        guess.
    guesses : list
        All attempts (each one contains a guess and its comparison to
        solution) the player has made.
        
    Methods
    -------
    
    """
    
    
    
    def __init__(self):
        """ """
        self._records = self._extraction()
        self.iteration = self._get_iteration(self._records)
        self.solution = self._get_solution(self._records)
        self.guesses = self._get_guesses(self._records)
        
    def _extraction(self):
        """ """
        records = []
        file = open("Save.csv", "r")
        for record in file:
            records.append(record)
        file.close()
        return records
            
    def _get_iteration(self, _records):
        """ """
        iteration = len(_records) - 1
        return iteration
    
    def _get_solution(self, _records):
        """ """
        cipher = _records[0]
        solution = save.decrypt_solution(cipher)
        return solution
    
    def _get_guesses(self, _records):
        """ """
        guesses = []
        for i in range(1, len(_records)):
            guess = save.restoring_guess(_records[i])
            guesses.append(guess)
        return guesses
    
    
        
        
    
        
        
        
l = Load()

print(l._records)
print(l.iteration)
print(l.solution)
print(l.guesses)