n = 999
print (n - n % 10) / 10
print (n % 100 - n % 10) / 10
print ((n - n % 10) / 10) % 10

def f(x):
    return -5*x**5 + 69*x**2-47

print "0:\t", f(0)
print "1:\t", f(1)
print "2:\t", f(2)
print "3:\t", f(3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years

    # Some code required
    return present_value*(1+rate_per_period)**periods
    
print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print future_value(500, .04, 10, 10)

# n - number of sides
# s - lenght of each side
import math
def regular_polygon_area(n,s):
    return (0.25*n*s**2)/(math.tan(math.pi/n))

print "5 sides, 7 inches:", regular_polygon_area(5, 7)
print "7 sides, 3 inches:", regular_polygon_area(7, 3)

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b
    
def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))   

def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print point_x * scale, point_y * scale

project_to_distance(2, 7, 4)
