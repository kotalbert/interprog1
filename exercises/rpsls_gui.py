""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for buttons and input fields # 6. 

GUI for Rock-paper-scissors-lizard-Spock game
"""

# Game logic copied from Mini project 1:

class Names_map:
    """
    Class for mapping names to numbers and numbers to names.
    It also implements the helper functions:
    
    number_to_name(number)
    name_to_number(name)
    
    The key idea of this program is to equate the strings
    "rock", "paper", "scissors", "lizard", "Spock" to numbers
    as follows:
    
    0 - rock
    1 - Spock
    2 - paper
    3 - lizard
    4 - scissors
    
    """
    # I will my maps on object initialization
    # note - double underscore: "__" means that function or data will not be visible from outside
    __names_map = dict()    # map: names to numbers
    __number_map = dict()   # map: numbers to names
    
    def __fill_names_map(self):
        """
        adding elements to names to numbers mapping
        """
        self.__names_map["rock"]        = 0
        self.__names_map["spock"]       = 1
        self.__names_map["paper"]       = 2
        self.__names_map["lizard"]      = 3
        self.__names_map["scissors"]    = 4
        
    # reversing the names to numbers in order to get number to names mapping
    def __reverse_names_map(self):
        for name in self.__names_map:
            number = self.__names_map[name]
            self.__number_map[number] = name      

    def __init__(self):
        self.__fill_names_map()
        self.__reverse_names_map()
    
    # I've decided to implement helper functions as a method of my dictionary holding class:
    
    def number_to_name(self, number):
        """
        helper function that returns a name corresponding to given number
        get() function will return "Number not found" if number not found
        """
        return self.__number_map.get(number, "Number not found")
    
    # 
    def name_to_number(self, name):
        """
        helper function that return a number corresponding to given name
        get() function will return "Name not found" if name not found
        """
        return self.__names_map.get(name.lower(), "Name not found")

import random
def rpsls(player_choice):
    """
    Game of RPSLS, implemented using Names_map class converting numbers to names and names 
    to numbers.
    """
    # creating the names map to get the helper functions 
    nm = Names_map()
    
    
    # print a blank line to separate consecutive games
    print 
        
    # print out the message for the player's choice
    print "Player chooses: %s" %player_choice 

    # convert the player's choice to player_number using the function name_to_number()
    player_number = nm.name_to_number(player_choice)

    # Validate player choice: if player_number is a number: proceed
    # else: exit function and print a messege
    if not isinstance(player_number, int):
        print "Invalid player choince."
        return 

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = nm.number_to_name(comp_number)
    
    
    # print out the message for computer's choice
    print "Computer chooses: %s" %comp_choice

    # compute difference of comp_number and player_number modulo five
    diff = (comp_number-player_number)%5

    # use if/elif/else to determine winner, print winner message
    if diff == 1 or diff == 2:
        print "Computer wins!"
    elif diff == 3 or diff ==4:
        print "Player wins!"
    else:
        print "Player and computer tie!"
        
        
# GUI implementation
# http://www.codeskulptor.org/#user39_oVMglvtVOfIRcbK.py

import simpleguitk as simplegui

frame = simplegui.create_frame("RPSLS", 200, 200, 200)
frame.add_input("Player choice", rpsls, 200)
frame.start()
    