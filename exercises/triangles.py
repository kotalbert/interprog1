# An Introduction to Interactive Programming in Python (Part 1)
# Challenges regarding triangle perimiter and area
# including chellenge 11. from functions excercises

import math
from string import split

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
    __area      = 0.0
    
    # calculate lenght of each side
    def __calc_sides(self):
        self.__a = self.__node1.distance(self.__node2)
        self.__b = self.__node2.distance(self.__node3)
        self.__c = self.__node1.distance(self.__node3)
    
    # http://en.wikipedia.org/wiki/Heron's_formula
    # semiperimeter
    def __calc_s(self):
        self.__s = 0.5*sum([self.__a, self.__b, self.__c])
    
    def __calc_perimeter(self):
        self.__perimeter= 2*self.__s
    
    # http://en.wikipedia.org/wiki/Heron's_formula
    # area of triangle
    def __calc_area(self):
        x = self.__s*(self.__s-self.__a)*(self.__s-self.__b)*(self.__s-self.__c)
        self.__area = math.sqrt(x)
    
    def __init__(self, node1, node2, node3):
        self.__node1 = node1
        self.__node2 = node2
        self.__node3 = node3
        
        self.__calc_sides()
        self.__calc_s()
        self.__calc_perimeter()
        self.__calc_area()
    
    def print_perimeter(self):
        print "Triangle %s, %s, %s has a perimeter of %.1f." \
        %(self.__node1, self.__node2, self.__node3, self.__perimeter)
        
    def print_area(self):
        print "Triangle %s, %s, %s has a area of %.1f." \
        %(self.__node1, self.__node2, self.__node3, self.__area)


# User input
def get_point(point_name):
    dlm = ','
    inp = raw_input("Enter coordinates for %s, spearated by '%s'." %(point_name, dlm)) 
    inp_splited = inp.split(dlm)
    
    try:
        x0 = float(inp_splited[0])
        x1 = float(inp_splited[1])
        return My_Point(x0, x1)
    except:
        print "Invalid point coordinates"
        quit()
 
x = get_point("x")
y = get_point("y")
z = get_point("z")
  
print x, y, z
t = My_Triangle(x,y,z)
t.print_area()
 
quit()
    
# Triangle 1    
n1 = My_Point(0,0)
n2 = My_Point(3,4)
n3 = My_Point(1,1)
t1 = My_Triangle(n1,n2,n3)
t1.print_perimeter()
t1.print_area()

# Triangle 2
n1 = My_Point(-2,4)
n2 = My_Point(1,6)
n3 = My_Point(2,1)
t2 = My_Triangle(n1,n2,n3)
t2.print_perimeter()
t2.print_area()

# Triangle 3
n1 = My_Point(10,0)
n2 = My_Point(0,0)
n3 = My_Point(0,10)
t3 = My_Triangle(n1,n2,n3)
t3.print_perimeter()
t3.print_area()