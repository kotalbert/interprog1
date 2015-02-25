# # An Introduction to Interactive Programming in Python (Part 1)
# Practice exercises for logic and conditionals

# 1. is_even
def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False
    
# Testing
print "1 is even:", is_even(1)
print "2 is even:", is_even(2)
    
# 2. is_cool
def is_cool(name):
    cool_names = ["Joe", "John", "Stephen"]
    if name in cool_names:
        return True
    else:
        return False

# Testing
print "Joe is cool:", is_cool("Joe")
print "Scott is cool:", is_cool("Scott")

# 3. is_lunchtime
def is_lunchtime(hour, is_am):
    hours = range(1,13)
    if hour not in hours:
        print "Invalid hour."
        return -1
    
    if (hour == 12 and not is_am) or (hour == 11 and is_am):
        return True
    else:
        return False

# Testing
print "10am is lunch time:", is_lunchtime(10, True)
print "12pn is lunch time:", is_lunchtime(12, False)
print "112pm is lunch time:", is_lunchtime(112, False)

# 4. is_leap_year
# http://en.wikipedia.org/wiki/Leap_year#Algorithm
def is_leap_year(year):
    if year%4 != 0: return False
    else:
        if year%100 != 0: return True
        else:
            if year%400 != 0: return False
            else: return True

#Testing
def test_leap_year(year):
    print "%d is leap year: %s" %(year, is_leap_year(year)) 

test_leap_year(2000)
test_leap_year(1996)
test_leap_year(1800)
test_leap_year(2013)

#5. interval_intersect 
def interval_intersect(a,b,c,d):
    if c<=b and a <= d: return True
    else: return False
    
#Testing

def test_interval_intersect(a,b,c,d):
    intersect = interval_intersect(a,b,c,d)
    print "Intervals [%d, %d] and [%d, %d] intersect: %s" %(a,b,c,d, intersect)

#Intervals [0, 1] and [1, 2] intersect.
test_interval_intersect(0,1,1,2)

#Intervals [1, 2] and [0, 1] intersect.
test_interval_intersect(1, 2, 0, 1)

#Intervals [0, 1] and [2, 3] do not intersect.
test_interval_intersect(0, 1, 2, 3)

#Intervals [2, 3] and [0, 1] do not intersect.
test_interval_intersect(2, 3, 0, 1)

#Intervals [0, 3] and [1, 2] intersect.
test_interval_intersect(0, 3, 1, 2)

# 6.  name_and_age 
def name_and_age(name, age):
    if age < 0:
        return "Error: Invalid age"
    else:
        return "%s is %d years old." %(name, age)
    
# Testing
print name_and_age("Joe Warren", 52)
print name_and_age("Scott Rixner", 40)
print name_and_age("John Greiner", -46)

# 7. Done in functions excercise.

# 8. name_lookup
def name_lookup(first_name):
    if first_name == "Joe": return "Warren"
    elif first_name == "Scott": return "Rixner"
    elif first_name == "John": return "Greiner"
    elif first_name == "Stephen": return "Wong"
    else: return "Error: Not an instructor"
    
# Testing
def test_name_lookup(first_name):
    print first_name, name_lookup(first_name)
    
test_name_lookup("Joe")
test_name_lookup("Scott")
test_name_lookup("John")
test_name_lookup("Stephen")
test_name_lookup("Mary")    

#9. pig_latin - simplified
def pig_latin(word):
    first_letter = word[0]
    rest_of_word = word[1 : ]
    
    vovel_list = ['a', 'e', 'i', 'o', 'u']

    if first_letter not in vovel_list:
        return rest_of_word+first_letter+"ay"
    else:
        return first_letter+rest_of_word+"way"
    
# Testing
def test_pig_latin(word):
    print "%s in pig latin is %s" %(word, pig_latin(word))

test_pig_latin("pig")
test_pig_latin("owl")
test_pig_latin("python")

# 10, Solution in the file: qyadratic.py