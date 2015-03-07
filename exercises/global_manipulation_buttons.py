""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for buttons and input fields # 3. 

Manipulate global variable count

Event handlers:
reset
increment
decrement
print_count

"""

import simpleguitk as simplegui

count = -1

def reset():
    global count
    count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def print_count():
    print count


button_width = 50    
frame = simplegui.create_frame("Manipulate count", 200, 200)
frame.add_button("Print count", print_count, button_width)
frame.add_button("Reset", reset, button_width)
frame.add_button("Increment", increment, button_width)
frame.add_button("Decrement", decrement, button_width)
frame.start()
