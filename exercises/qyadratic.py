# # An Introduction to Interactive Programming in Python (Part 1)
# Logic excercise 10.: quadratic equation

import math

def smaller_root(a,b,c):
    
    d = b**2 - 4*a*c
        
    if d > 0: 
        x1 = (-b+math.sqrt(d))/ (2*a)
        x2 = (-b-math.sqrt(d))/ (2*a) 
        return min(x1,x2)
    elif d == 0: 
        x1 = (-b+math.sqrt(d))/2*a
        return x1
    else: print "Error: No real solutions"
    
#Testing:
def test_smaller_root(a,b,c):
    sm_root = smaller_root(a,b,c)
    print "The smaller root of %dx^2 + %dx + %d is: %s" %(a,b,c,sm_root)
    
test_smaller_root(1, 2, 3)
test_smaller_root(2, 0, -10)
test_smaller_root(6, -3, 5)
