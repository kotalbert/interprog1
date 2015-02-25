# An Introduction to Interactive Programming in Python (Part 1)
# Practice exercises for functions

# 1. miles_to_feet function
def miles_to_feet(miles):
    return miles*5280

print miles_to_feet(1)

# 2.  total_seconds 
def total_seconds(hours, minutes, seconds):
    return 60*(60*hours + minutes) + seconds

print total_seconds(7, 21, 37)

# 3. rectangle_perimeter 
def rectangle_perimeter(width, height):
    return 2*width + 2*height

print rectangle_perimeter(2, 6)

#4. rectangle_area
def rectangle_area(width, height):
    return width*height

print rectangle_area(2, 6)

# 5. circle_circumference 
import math
def circle_circumference (radius):
    return 2*math.pi*radius

print circle_circumference(8)

# 6. circle_area
def circle_area(radius):
    return math.pi*radius**2

print circle_area(8)

#7. future_value 
def future_value(present_value, annual_rate, years):
    return present_value * (1+0.01*annual_rate)**years

print future_value(1000, 7, 10)

# 8. name_tag 
def name_tag(first_name, last_name):
    return "My name is %s %s." %(first_name, last_name)

print name_tag("Johhny", "Walker")

# 9. name_and_age 
def name_and_age(name, age):
    return "%s is %d years old." %(name, age)

print name_and_age("John", 21)

# 10. & 11. are in triangles.py

# 12. is in print_digits.py

# 13. is in powerball.py


