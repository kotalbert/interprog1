""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for buttons and input fields # 1. 
print_hello
print_goodbye
"""
import simpleguitk as simplegui


def print_hello():
    print "Hello"

def print_goodbye():
    print "Goodbye"
    
frame = simplegui.create_frame("Hello and Goodbye", 200, 200)

frame.add_button("Hello", print_hello, 50)
frame.add_button("Goodbye", print_goodbye, 50)

frame.start()


    