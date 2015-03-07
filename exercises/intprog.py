# # An Introduction to Interactive Programming in Python (Part 1)
# Practice exercise for interactive applications

def hl():
    print "*" * 20

# 1. pring_goodbye

def print_goodbye():
    message = "Goodbye"
    print message
    
# Tests

message = "Hello"
print message
print_goodbye()
print message

message = "Ciao"
print message
print_goodbye()
print message

hl()

# 2.  set_goodbye

def set_goodbye():
    global message
    message = "Goodbye"
    print message
    
# Tests 

message = "Hello"
print message
set_goodbye()
print message

message = "Ciao"
print message
set_goodbye()
print message

hl()

# 4. "My first frame"
import simpleguitk as simplegui


# message = "My first frame!"
# 
# # Handler for mouse click
# def click():
#     print message
# 
# # Create a frame and assign callbacks to event handlers
# frame = simplegui.create_frame("My first frame", 100, 200)
# frame.add_button("Click me", click)
# frame.start()

# 5. "My second frame"

message = "My second frame!"

# Handler for mouse click
def click():
    print message

frame = simplegui.create_frame("My second frame", 200, 100) 

# Assign callbacks to event handlers
frame.add_button("Click me", click)

# Start the frame animation
frame.start()

