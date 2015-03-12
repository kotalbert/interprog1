""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for timers # 1. 

Counter to console.
"""

# Counter ticks

###################################################
# Student should add code where relevant to the following.

import simpleguitk as simplegui

counter = 0

# Timer handler
def tick():
    global counter
    print counter
    counter += 1

# create timer
timer = simplegui.create_timer(1000, tick)
frame = simplegui.create_frame("Ticks.", 200, 200)
timer.start()
frame.start()