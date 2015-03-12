""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for drawing # 4. 

Format time
"""
import simpleguitk as simplegui
import math

# Define a function that returns formatted minutes and seconds
def format_time(seconds):
    minutes = math.floor(seconds // 60)
    remaining_sec = seconds - minutes * 60
    
    return "%d minutes and %d seconds" %(minutes, remaining_sec)


###################################################
# Tests

print format_time(23)
print format_time(1237)
print format_time(0)
print format_time(1860)

###################################################
# Output to console
#0 minutes and 23 seconds
#20 minutes and 37 seconds
#0 minutes and 0 seconds
#31 minutes and 0 seconds