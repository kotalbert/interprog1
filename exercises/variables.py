# An Introduction to Interactive Programming in Python (Part 1)
# Practice exercises for variables and assignments    

# 1. Compute the number of feet corresponding to __a number of miles:
def miles_to_feet(miles):
    return float(miles * 5280)

def print_miles_to_feet(miles):
    print "%.1f miles equals %.1f feet" %(miles, miles_to_feet(miles))
    
print_miles_to_feet(13)
print_miles_to_feet(57)
print_miles_to_feet(82.67)

# 2. Calculate total seconds:
class My_Time(object):
    h = 0
    m = 0
    __s = 0
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.__s = s
        
    def __repr__(self):
        return "%d::%d::%d" %(self.h, self.m, self.__s)
    
    def total_seconds(self):
        return 60*(60*self.h + self.m) + self.__s
    
    def print_total_seconds(self):
        print "%d hours, %d minutes, and %d seconds totals to %d seconds" \
        %(self.h,self.m, self.__s, self.total_seconds())        

time1 = My_Time(7,21,37)
time2 = My_Time(10,1,7)
time3 = My_Time(1,0,1)

time1.print_total_seconds()
time2.print_total_seconds()
time3.print_total_seconds()

# 3. & 4. Rectangle perimeter and area:
class My_Rectangle(object):
    w = 0
    h = 0
    perimeter = 0
    area = 0
    
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.perimeter = 2*w + 2*h
        self.area = w*h
        
    def __repr__(self):
        
        return "A rectangle %d inches wide and %d \
inches high h__as a perimeter of %d inches and area of %d square inches." \
    %(self.w,self.h, self.perimeter, self.area)
        

r1 = My_Rectangle(4,7)
r2 = My_Rectangle(7,4)
r3 = My_Rectangle(10,10)

print r1
print r2
print r3

# 5. , 6., 7., 8., 9., 10. done in previous program

# 11. Calculate the area of triangle:

# Point class from __a previous excercise.
import math

class My_Point(object):
    __x   = 0.0
    __y   = 0.0
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def __repr__(self):
        return "(%g, %g)" %(self.__x,self.__y)

    def distance(self, other_point):
        return math.sqrt((self.__x - other_point.__x)**2+(self.__y - other_point.__y)**2)
        
class My_Triangle(object):
    __node1 = My_Point(0,0)
    __node2 = My_Point(0,0)
    __node3 = My_Point(0,0)
    
    __a = 0.0 # side __a: __node1 : __node2
    __b = 0.0 # side __b: __node2 : __node3
    __c = 0.0 # side __c: __node1 : __node3
    __s = 0.0
    __perimeter = 0.0
    
    def __calc_sides(self):
        self.__a = self.__node1.distance(self.__node2)
        self.__b = self.__node2.distance(self.__node3)
        self.__c = self.__node1.distance(self.__node3)
    
    def __calc_s(self):
        self.__s = 0.5*sum([self.__a, self.__b, self.__c])
    
    def __calc_perimeter(self):
        x = self.__s*(self.__s-self.__a)*(self.__s-self.__b)*(self.__s-self.__c)
        self.__perimeter = math.sqrt(x)
    
    def __init__(self, node1, node2, node3):
        self.__node1 = node1
        self.__node2 = node2
        self.__node3 = node3
        
        self.__calc_sides()
        self.__calc_s()
        self.__calc_perimeter()
    
    def print_perimeter(self):
        print "Triangle %s, %s, %s has a perimeter of %.1f." \
        %(self.__node1, self.__node2, self.__node3, self.__perimeter)
    
# Triangle 1    
n1 = My_Point(0,0)
n2 = My_Point(3,4)
n3 = My_Point(1,1)
t1 = My_Triangle(n1,n2,n3)
t1.print_perimeter()



# Triangle 2
n1 = My_Point(-2,4)
n2 = My_Point(1,6)
n3 = My_Point(2,1)
t2 = My_Triangle(n1,n2,n3)
t2.print_perimeter()

# Triangle 3
n1 = My_Point(10,0)
n2 = My_Point(0,0)
n3 = My_Point(0,10)
t3 = My_Triangle(n1,n2,n3)
t3.print_perimeter()
