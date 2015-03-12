""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for drawing # 3. 

Display an X
"""
import simpleguitk as simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text("X", (0,36), 48, "White")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Display an X", 96, 96)
frame.set_draw_handler(draw)

# Start the frame animation
frame.start()