from mp_1_rpsls import *

def cp(fnc_name):
    print "Testing:\t%s" %fnc_name

def tend(fnc_name):
    print "Ending test:\t%s" %fnc_name

nm = Names_map()

def test_name_to_number():
    cp("name_to_number")
    print nm.name_to_number("rock")
    print nm.name_to_number("Spock")
    print nm.name_to_number("paper")
    print nm.name_to_number("lizard")
    print nm.name_to_number("scissors")
    tend("name_to_number")

def test_number_to_name():
    cp("number_to_name")
    print nm.number_to_name(0)
    print nm.number_to_name(1)
    print nm.number_to_name(2)
    print nm.number_to_name(3)
    print nm.number_to_name(4)
    tend("number_to_name")

def test_game():
    cp("rosls")
    rpsls("rock")
    rpsls("Spock")
    rpsls("paper")
    rpsls("lizard")
    rpsls("scissors")    
    tend("rpsls")
    
test_name_to_number()
test_number_to_name()
# test_game()


print nm.name_to_number("SpoCkqq")
print nm.number_to_name(11)

