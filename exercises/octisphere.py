# Example Mini-Project:
# THE MYSTICAL OCTOSPHERE! by Andrea Crain

import random

def number_to_fortune(number):
    if number not in range(8):
        return "Input out of range: %d" %number
    
    octosphere_dict = {0    : "Yes, for sure!",
                       1    : "Probably yes.",
                       2    : "Seems like yes...",
                       3    : "Definitely not!",
                       4    : "Probably not.",
                       5    : "I really doubt it...",
                       6    : "Not sure, check back later!",
                       7    : "I really can't tell",                       
                       }
    
    return octosphere_dict[number]


    
def mystical_octosphere(question):
    print question
    print "You shake the mystical octosphere."
    answer_number = random.randrange(8)
    answer_fortune = number_to_fortune(answer_number)
    print "The cloudy liquid swirls, and a reply comes into view..."
    print "The mystical octosphere says..."
    print answer_fortune
    
    
qst = raw_input("Enter your question.")
mystical_octosphere(qst)

#Testing
 
# print number_to_fortune(0)
# print number_to_fortune(1)
# print number_to_fortune(2)
# print number_to_fortune(3)
# print number_to_fortune(4)
# print number_to_fortune(5)
# print number_to_fortune(6)
# print number_to_fortune(7)
# print number_to_fortune(19)
# 
# 
# mystical_octosphere("Will I get rich?")
# mystical_octosphere("Are the Cubs going to win the World Series?")