""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for buttons and input fields # 2. 

Manipulate global variable color

print_color
set_red
set_blue

"""

import simpleguitk as simplegui

color = "blue"

def print_color():
    print color
    
def set_red():
    global color
    color = "red"

def set_blue():
    global color
    color = "blue"

button_width = 50 
frame = simplegui.create_frame("Manipulating color", 200, 200)
frame.add_button("Print color", print_color, button_width)
frame.add_button("Set red", set_red, button_width)
frame.add_button("Set blue", set_blue, button_width)
frame.start()