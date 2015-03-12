"""
An Introduction to Interactive Programming in Python (Part 1)
Mini-project #3: "Stopwatch: The Game"
http://www.codeskulptor.org/#user39_YXUrGirFbT0P1mP.py
"""

import simpleguitk as sg

# define global variables
ticks   = 0
timer_is_running = False
tens_of_second = 0
hits    = 0
misses  = 0

# constants for GUI
CANVAS_HEIGHT   = 300
CANVAS_WIDTH    = 300
CONTROL_WIDHT   = 200

def format_time(t):
    """
    Helper function format_time that converts time
    in tenths of seconds into formatted string A:BC.D
    """
    total_seconds = t//10
    minutes = total_seconds//60
    seconds = total_seconds - minutes*60
    tens = t - 10*(minutes*60+seconds)
    
    # %02d format ensures a leading 0 in second count
    out_str = "%d:%02d.%d" % (minutes, seconds, tens)
    
    return out_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    """Button handler for starting the stopwatch"""
    global timer_is_running
    timer.start()
    timer_is_running = True

def stop_handler():
    """
    Button handler for stoping the stopwatch
    checks if player stopped the game in the right moment
    """
    
    global timer_is_running
    
    global hits
    global misses
    
    timer.stop()
    
    # Changes the score only if the timer is running
    if timer_is_running:
        if tens_of_second == 0:
            hits += 1
        else:
            misses += 1
            
    timer_is_running = False

def reset_handler():
    """
    Button handler for resetting the timer and game score.
    """
    global ticks
    global hits
    global misses
    
    ticks   = 0
    hits    = 0
    misses  = 0
    
def ticker():
    """
    Time handler for the game
    Calculates if current time is a full second so game score
    can be measured.
    """
    
    global ticks
    global tens_of_second
    ticks += 1
    tens_of_second = ticks%10

# define draw handler
def draw(canvas):
    """
    Drawing the timer and score on the canvas.
    Setting text to be in the middle of canvas and text height to be
    1/10 of canvas height.
    Score will be displayed in 1/10 of canvas height and width, in
    green text with size of 1/20 of canvas height
    """
    
    canvas.draw_text(format_time(ticks), [CANVAS_WIDTH//2, CANVAS_HEIGHT//2], \
                     CANVAS_HEIGHT//10, "White")
    
    score = "%d/%d" %(hits, misses)
    canvas.draw_text(score,[CANVAS_WIDTH//10, CANVAS_HEIGHT//10], \
                     CANVAS_HEIGHT//20, "Green")

# create frame
frame = sg.create_frame("Stopwatch The Game", CANVAS_WIDTH, CANVAS_HEIGHT,\
                        CONTROL_WIDHT)
frame.set_draw_handler(draw)


timer = sg.create_timer(100, ticker)

# register event handlers
frame.add_button("Start", start_handler, CONTROL_WIDHT)
frame.add_button("Stop", stop_handler, CONTROL_WIDHT)
frame.add_button("Reset", reset_handler, CONTROL_WIDHT)

# start frame
frame.start()