""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for timers # 2. 

Timer buttons control.
"""

# Counter with buttons

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1
    
# Event handlers for buttons    
def timer_start():
    timer.start()

def timer_stop():
    timer.stop()

def timer_reset():
    global counter
    counter = 0
    
    
# Create frame and timer

frame = simplegui.create_frame("Counter with buttons", 200, 200)
timer = simplegui.create_timer(1000, tick)
frame.add_button("Start timer", timer_start, 150)
frame.add_button("Stop timer",  timer_stop, 150)
frame.add_button("Reset timer", timer_reset, 150)

# Start timer
timer.start()
frame.start()