""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for drawing # 1. 

It works!
"""
import simpleguitk as simplegui

# Draw handler
def draw(canvas):
    canvas.draw_text("It works!",[120, 112], 48, "Red")
    

# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("It works", 400, 200)
frame.set_draw_handler(draw)
frame.start()