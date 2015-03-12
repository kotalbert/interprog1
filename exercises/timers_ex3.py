""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for timers # 3. 

Canvas color with timer.
"""

import simpleguitk as simplegui

color = "Red"

# Timer handler
def tick():
    global color
    
    if color == "Red":
        color = "Blue"
    else:
        color = "Red"
        
    frame.set_canvas_background(color)
         
# Create frame and timer
frame = simplegui.create_frame("Canvas with timer", 200, 200)
frame.set_canvas_background(color)

timer = simplegui.create_timer(1000, tick)

# Start timer
timer.start()
frame.start()