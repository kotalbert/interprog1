""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for buttons and input fields # 5. 

Text input into pig latin

"""

import simpleguitk as simplegui



#9. pig_latin - simplified
def pig_latin(word):
    """Simplified pig latin game"""
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    vovel_list = ['a', 'e', 'i', 'o', 'u']

    if first_letter not in vovel_list:
        return rest_of_word+first_letter+"ay"
    else:
        return first_letter+rest_of_word+"way"
    
def print_pig_latin(word):
    """
    Text input handler,
    Print pig latin into console
    """
    print pig_latin(word)
    
frame = simplegui.create_frame("Pig latin", 200, 200)
frame.add_input("Insert text", print_pig_latin, 100)
frame.start()
