""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for drawing # 2. 

This is easy
"""
import simpleguitk as simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text("This is easy?", (100,100), 12, "White")

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("This is easy", 400, 200)
frame.set_draw_handler(draw)


# Start the frame animation
frame.start()
