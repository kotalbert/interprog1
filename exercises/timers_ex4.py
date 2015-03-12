""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for timers # 4. 

Expanding circle by timer
"""

import simpleguitk as simplegui

WIDTH               = 200
HEIGHT              = 200
radius_increment    = 1
radius              = 1


# Timer handler
def increment_radius():
    global radius
    global radius_increment
    
    radius += radius_increment
    
    # Reverting counter if circle reaches limits
    if radius == 0 or radius == HEIGHT:
        radius_increment = - radius_increment
    
# Draw handler
def draw(canvas):
    canvas.draw_circle([WIDTH, HEIGHT], radius, 1, "White")
    
        
# Create frame and timer
timer = simplegui.create_timer(1, increment_radius)
frame = simplegui.create_frame("Increment circle", WIDTH*2, HEIGHT*2)
frame.set_draw_handler(draw)

# Start timer
timer.start()
frame.start()
