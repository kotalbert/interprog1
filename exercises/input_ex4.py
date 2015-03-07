""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for buttons and input fields # 4. 

Echo text input to console

"""

import simpleguitk as simplegui

def echo_input(txt):
    print txt
    
frame = simplegui.create_frame("Echo input", 200, 200)
frame.add_input("Enter text", echo_input, 100)
frame.start()