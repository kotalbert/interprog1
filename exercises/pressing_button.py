""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for timers # 5. 

Reflex tester
"""

import simpleguitk as simplegui

total_ticks = 0
first_click = True


# Timer handler
def tick():
    global total_ticks     
    total_ticks += 1
    
    
def measure_time():
    time_elapsed = total_ticks / 100.0
    print "Elapsed time:\t %g seconds" %time_elapsed  
    
# Button handler
def click():
    global first_click
    global total_ticks
    
    if first_click:
        total_ticks = 0
        print "Starting measurment."
    else:
        measure_time()
    
    first_click = not first_click    
    
# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
timer.start()
frame.start()