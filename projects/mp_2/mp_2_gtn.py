"""
An Introduction to Interactive Programming in Python (Part 1)
Mini-project #2: "Guess the number game"

"""

import random
import math
import simpleguitk as simplegui

# helper function to start and restart the game
def new_game():
    """initialize global variables used in your code here"""
    set_globals(0, 100)
    new_game_msg()
 
def new_game_msg():
    """Prints basic information on new game that started. """
    print
    print '*' * 25
    print "Starting new game."
    print "Guess the number in range: [%d,%d)" %(lo, hi)
    print "Guesses left: %d" %guesses_left
    print "Secret number: %d" %secret_number

def set_globals(lo_par, hi_par):
    """
    Helper function setting the global variables values.
    Computes the number to be guessed and sets the maximal numbers of
    guesses for given lo_par : hi_par parameters,
    which in turn sets the global range variables: hi and lo
    .
    """
    global secret_number
    global guesses_left
    global hi
    global lo
    
    hi = hi_par
    lo = lo_par
    
    secret_number = random.randrange(lo, hi)
    
    """ 
    Calculating the maximal numbers of guesses as 
    base 2 logarithm of a parameters hi, lo range 
    and then ceiling it to get the integer value.
    """
    guesses_left = int(math.ceil(math.log(hi-lo, 2)))
    
def miss_guess():
    """
    Helper function decreasing number of guesses left and printing 
    the the number to the console
    """
    global guesses_left
    guesses_left -= 1
    print "Guesses left: %d" %guesses_left

def end_game():
    """
    Helper function that restarts the game if player fails to guess
    the correct number.
    """
    print "You failed to guess the number."
    new_game()
    
    
# define event handlers for control panel
def range100():
    """ 
    button that changes the range to [0,100) 
    and starts a new game
    """ 
    set_globals(0, 100)
    new_game_msg()
    
def range1000():
    """ 
    button that changes the range to [0,1000) 
    and starts a new game     
    """
    set_globals(0, 1000)
    new_game_msg()
    
def input_guess(guess_txt):
    """main game logic """
    
    """ 
    Exception handler: if program is unable to convert
    input to integer, the number of guesses left is decreased
    and a message is printed to output window.
    """	
    try:
        guess_int = int(guess_txt)
    except:
        print "Invalid guess."
        miss_guess()
        if guesses_left > 0:
            return
        else:
            end_game()
            return
    
    """
    While loop restricts the number of guesses to the number 
    of guesses left and restarts the game if player looses.
    """
    print "Your guess: %d" %guess_int
    
    if guesses_left > 0:
        if guess_int < secret_number:
            print "Higher"
            miss_guess()
        elif guess_int > secret_number:
            print "Lower"
            miss_guess()
        else:
            print "Correct, restarting the game!"
            new_game()
    else:
        end_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_input("Enter your guess", input_guess, 200)
frame.add_button("New game: range: [0, 100)", range100, 200)
frame.add_button("New game: range: [0, 1000)", range1000, 200)

# call new_game 
new_game()
frame.start()

# http://www.codeskulptor.org/#user39_B9Sv8XwwMbOwSzz.py
