# An Introduction to Interactive Programming in Python (Part 1)
# Practice exercises for expressions 

# 1. Number of feet in 13 miles:

feet_in_13_miles = 13 * 5280 #There are 5280 feet in a mile.
print "There are %d in 13 miles" %feet_in_13_miles

# 2. Number of seconds in 7 hours, 21 minutes and 37 seconds:

total_seconds = 7*3600+21*60+37
print "Total numer of seconds: %d" %total_seconds

# 3. The perimeter of a rectangle with sides 
# of length 4 and 7 inches:

rec_w = 4
rec_h = 7

rec_perimeter = 2*rec_w + 2*rec_h
print "Rectangle perimeter is %d" %rec_perimeter

# 4. The area of a rectangle with sides of length 4 and 7 inches:

rec_area = rec_w * rec_h
print "Rectangle area is %d" %rec_area

# 5. Circumference in inches of a circle whose radius is 8 inches:
r = 8
pi = 3.14
circumference = 2*pi*r
print "Circle circumference of radius %d is %g" %(r, circumference)

# 6. Area of circle whose radious is 8 inches:
radius = pi * r ** 2
print "Circle area of radius %d is %g" %(r, radius)

# 7. Value of 1k USD compounded at 7% interest for 10 years:
i = 7 # percent
v = 1000 
t = 10
fv = v * (1+0.01*i)**t 
print "Future Value of %g USD over %d years at %d percent is %g USD" \
%(v, t, i, fv) 

# 8. String concatanation:
s1 = "My name is"
s2 = "Joe"
s3 = "Warren"
text = " ".join([s1,s2,s3]) # join list of strings
print text 

# 9. Print "Joe Warren is 52 years old." 
# from the string "Joe Warren" and the number 52: 
name = "Joe Warren"
age = 52
print "%s is %d years old" %(name, age)

# 10. Calculate distance between point (2,2) and (5,6)

import math

class Point(object):
    x   = 0.0
    y   = 0.0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "(%g, %g)" %(self.x,self.y)

    def distance(self, other_point):
        return math.sqrt((self.x - other_point.x)**2+(self.y - other_point.y)**2)
        
p1 = Point(2,2)
p2 = Point(5,6)

print "The distance between %s and %s is %g" \
%(p1, p2, p1.distance(p2))





