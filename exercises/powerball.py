# # An Introduction to Interactive Programming in Python (Part 1)
# Functions excercise 13.: powerball lottery game.

import random

def powerball():
    SIZE = 5
    MAX_DRAWN = 60
    MAX_POWERBALL = 36
    drawn_numbers = []
    
    # Drawing numbers from [0, MAX_DRAWN) range
    for i in range (SIZE):
        drawn_numbers.append(str(random.randrange(0,MAX_DRAWN)))

    # Array is indexed starting 0, 
    # slice [:-1] returns all but last elements
    # last item is at [-1] index:
    
    drawn_str = ", ".join(drawn_numbers[:-1])
    last = drawn_numbers[-1]
    
    # Drawing powerball from [0, MAX_POWERBALL) range
    powerball_number = random.randrange(0,MAX_POWERBALL)
    
    return "Today's numbers are %s and %s. The Powerball number is %d." %(drawn_str, last, powerball_number)
    
print powerball()
    