# -*- coding: utf-8 -*-
"""
Created on Sat May  7 14:20:12 2022

@author: Codeoliocos
"""

import mm_functions as mm_fun

class Combination():
    
    """ This is a basic class, for every combination of cells and
    colours. This class contains two methods- position (a 
    cell-colour dictionary) and colour scheme (list of colours)
    
    """
    
    def __init__(self, position):
        
        self.position = position
        self.colour_scheme = mm_fun.preparing_scheme(position)
        

class GameState():
    """ This class one day will recieve proper documentation"""
    
    def __init__(self, iteration):
        
        self.iteration = 0


class NewTry(Combination):
    
    """ This class is for guesses only. It inherits both methods of
    it's parent class (Combination), but also contains bunch of other
    methods, as a steps to most important one - the result. It 
    returns a dictionary with position of player's guess and it's 
    matches with original (coded) position. Then it will be displayed
    at 
    (at or on? I'm not sure about that one...)
    GUI
    
    """
    
    def __init__(self, position, solution):
        
        super().__init__(position)
        
        self.position = position
        self.colour_scheme = mm_fun.preparing_scheme(position)
        
        self.solution_position = solution.position
        self.solution_colour_scheme = solution.colour_scheme
        
        self.abs_matches = mm_fun.compare_positions(
              self.solution_position, self.position)
        
        
        self.colour_matches = mm_fun.compare_colours(
                         self.solution_colour_scheme, 
                self.colour_scheme, self.abs_matches)
        
        
        self.reply = mm_fun.compose_reply(self.abs_matches, 
                                          self.colour_matches)
        
        self.result = mm_fun.compose_result(self.position, 
                                            self.reply)
        
        
class Turn():
    """  """
    
    def __init__(self, position, solution):
        """  """
        
        self.position = position
        self.solution = solution
    







