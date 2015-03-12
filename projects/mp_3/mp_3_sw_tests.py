from mp_3_sw import format_time

# Test the format

import simpleguitk as sg

def format_test(ticks):
    print format_time(ticks)

tick = 0

format_test(0)
format_test(11)
format_test(321)
format_test(613)

def print_format():
    global tick
    tick += 1
    format_test(tick)

timer = sg.create_timer(100, print_format)
timer.start()