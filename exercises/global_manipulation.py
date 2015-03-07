""" 
An Introduction to Interactive Programming in Python (Part 1)
Practice exercises for buttons and input fields # 3. 

Manipulate global variable count

functions:
reset
increment
decrement
print_count

"""

count = -1

def reset():
    global count
    count = 0

def increment():
    global count
    count += 1

def decrement():
    global count
    count -= 1

def print_count():
    print count

# Test

# note that the GLOBAL count is defined inside a function
reset()        
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()