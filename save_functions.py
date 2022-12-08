# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:52:24 2022

@author: Codeolicos
"""

""" This module contains the most basic functions for saves and loads"""

import csv
from random import randint

colours = ["red", "orange", "yellow", "green", 
           "cyan", "blue", "purple"]
    
def cleaning_save_file():
    """
    This function re-creates save file and by that cleans all 
    records from it.
    
    Arguments:
        None
    Returns:
        None
    """
    
    file = open("Save.csv", 'w')
    file.close()

def decrypt_solution(cipher):
    """
    This function loads number sequence (encrypted colour scheme 
    of solution) from save file, decodes it back, creates solution 
    dictionary and returns it.
    
    Arguments:
        cipher : str
    Returns:
        solution : dict
    """
    
    solution = dict()
    cell_number = 1
    
    for i in range(1, 15):
        if i % 3 == 0:
            colour_index = int(cipher[i-1])
            solution[cell_number] = colours[colour_index]
            cell_number += 1
            
        # This 
    
    return solution

def encrypt_solution(solution):
    """
    This function encrypts solution, making harder to see solution 
    in the save file.
    
    Arguments:
        solution : dict
    Returns:
        cipher : str
    """
    
    cipher = ""
    cell_number = 1
    
    for i in range(1, 15):
        if i % 3 == 0:
            digit = colours.index(solution[cell_number])
            cell_number += 1
        else:
            digit = randint(0, 9)
        cipher += str(digit)
    
    cipher += "\n"
    return cipher

def recording_cipher(cipher):
    """This function writes encrypted solution into the save file. 
    
    Arguments:
        cipher : str
    Returns:
        None
    """
    
    file = open("Save.csv", 'a')
    file.write(cipher)
    file.close()
    
def creating_record(guess):
    """
    This function takes player's guess (attempt and reply to this 
    attempt), turns it into a string of colours and adds this string
    to the save file.
    
    Arguments:
        guess : dict
    Returns:
        None
    """
    
    record = ""
    position = guess['position']
    reply = guess['reply']
    file = open('Save.csv', 'a')
    
    for i in range(1, 5):
        colour = position[i]
        record += colour + ", "
        
    for i in range(1, 5):
        colour = reply[i]
        record += colour + ", "
        
    last_comma = record.rfind(",")
    record = record[:last_comma]
    record += " \n"
        
    file.write(record)
    file.close()
    
def restoring_guess(record):
    """
    This function decomposes a record from save file into player's guess 
    and comparison to the solution.
    
    Arguments:
        record : str
    Returns:
        guess : dict
    """
    
    guess = dict()
    position = dict()
    reply = dict()
    
    full_colour_scheme = [colour for colour in record.split()]
    
    # i - 1 for colours [0:3], i + 3 for colours [4:7]
    for i in range (1, 5):
        position[i] = full_colour_scheme[i - 1]
    for i in range(1, 5):
        reply[i] = full_colour_scheme[i + 3]
            
    guess["position"] = position
    guess["reply"] = reply
    
    return guess

