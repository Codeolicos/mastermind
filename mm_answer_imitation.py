# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:06:49 2022

@author: Codeoliocos
"""

from random import randint

import mm_functions as mm_fun


def reply_imitation():
    
    black_cells = randint(0, 3)
    grey_first = randint(0, 3)
    empty_cells = 4 - black_cells

    if grey_first <= empty_cells:
        grey_cells = grey_first
    else:
        grey_cells = empty_cells
        
    reply = dict()
    
    for i in range(1, 5):
        
        if black_cells != 0:
            reply[i] = "black"
            black_cells -= 1
            
        elif grey_cells != 0:
            reply[i] = "grey"
            grey_cells -= 1
            
        else:
            reply[i] = "white"
            
    return reply

def answer_imitation():
    position = mm_fun.generate_solution()
    reply = reply_imitation()
    
    answer = dict()
    
    answer["position"] = position
    answer["reply"] = reply
    
    return answer


    