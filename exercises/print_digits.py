# # An Introduction to Interactive Programming in Python (Part 1)
# Functions excercise 12.: printing tens and ones in a number.
# function that takes integer number in the range [0,100) and prints:
# "The tens digit is %, and the ones digit is %."

def print_digits(number):
    
    if number not in range(0,100):
        print "%d is not in range [0, 100)." %number
        quit()
    else:
        tens = number//10;
        ones = number%10;
        print "The tens digit is %d, and the ones digit is %d." \
        %(tens, ones)
