# -*- coding: utf-8 -*-
"""
Created on Sat May  7 10:43:32 2022

@author: Codeolicos
"""

from random import choice

colours = ["red", "orange", "yellow", "green", 
           "cyan", "blue", "purple"]




def generate_solution():
    
    """ 
    This function generates combination of colours player 
    would try to guess. 
    
    Arguments:
        None
    Returns:
        solution : dict
    """
    
    solution = dict()
    
    for i in range(1, 5):
        solution[i] = choice(colours)
        
    return solution




def preparing_scheme(position):
    
    """ 
    This function makes colour scheme of combination to find 
    matches of just colours, ignoring the position.
    
    Arguments:
        position : dict
    Returns:
        colour_scheme : list
    """
        
    colour_scheme = []
    
    for cell in position:
        colour_scheme.append(position[cell])
        
    return colour_scheme
    



def compare_positions(solution_position, new_try_position):
    
    """ 
    Compares coded and guessed combinations by the colour 
    AND by the position then returns the number of full matches.
    
    Arguments:
        solution_position : dict
        new_try_position : dict
    Returns:
        abs_matches : int
    """
    
    abs_matches = 0
    
    for i in range(1, 5):
        if solution_position[i] == new_try_position[i]:
            abs_matches += 1
            
    return abs_matches




def compare_colours(solution_colours, new_try_colours, abs_matches):
    
    """ 
    This functions compares combinations by colours only, it finds the 
    number of all colours matches and substruct the number of absolut 
    matches (where colours mathes at the same position), so only mathes 
    of colours on different positions remains.
    
    Arguments:
        solution_colours : dict
        new_try_colours : dict
        abs_matches : int
    Returns:
        colour_matches : int
    """
    
    all_matches = 0
    
    for colour in solution_colours:
        if colour in new_try_colours:
            new_try_colours.remove(colour)
            all_matches += 1
            
    colour_matches = all_matches - abs_matches
    return colour_matches




def compose_reply(abs_matches, colour_matches):
    
    """ 
    Creates a dictionary with black cells as absolute matches,
    grey cells as only colour matches.
    
    Arguments:
       abs_mathes : int
       colour_matches : int
    Returns:
        reply : dict
    """
    
    reply = dict() 
   
    for i in range(1, 5):
       
        if abs_matches != 0:
            reply[i] = "black"
            abs_matches -= 1
            
        elif colour_matches != 0:
            reply[i] = "grey"
            colour_matches -= 1
            
        else:
            reply[i] = "white"
        
    return reply


           
def compose_result(position, reply):
    
    """
    This function composes a dictionary with 2 dictionaries: 
    position (cells and colours they contain) and reply (cells
    and colours of matches they contain).  It will be used by
    GUI for display of player's guess and result of this 
    guess.
    
    Arguments:
        position : dict
        reply : dict
    Returns:
        result : dict
    """
    
    result = dict()
    
    result["position"] = position
    result["reply"] = reply
    
    return result


def victory_check(reply):
    """ 
    This function checks was player's attempt successful.
    
    Arguments:
        reply : dict
    Returns:
        is_correct_guess : bool
    """
    
    # By default this function has state "True" and it remains like this 
    # while each reply cell is black. First grey/white cell will change
    # function state to "False" and break the cycle.
    
    is_correct_guess = True
    for i in range(1, 5):
        if reply[i] != "black":
            is_correct_guess = False
            break
    return is_correct_guess
    







def q():
    pass

