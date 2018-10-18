'''
Title: Cannon Operator
Name: Harleen Bajwa
Date: 10/10/18
'''
## import ##
import math

## variable ##
gravity = 9.81

# no input 1 output
def intro():
    print(
    """
                  __
                 |  \\
                 |   \\
    |\\           |    \\
    | \\          |_____\\
    |__\\         |_______
    |__----------|      /
 __|  +    +     +     /
|_____________________/
""")
    print("WELCOME TO THE CANNON OPERATOR PROGRAM! IN THIS PROGRAM THERE ARE 3 SCENAIROS WHICH CAN BE CALCULATED.")
    print("Scenairo 1: horizontal cannon.")
    print("Scenairo 2: angled cannon towards ship at same level.")
    print("Scenairo 3: angled cannon towards ship at lower but far away")
    get_scenario()
    return choice

# 1 input no output
def get_scenario():
    try:
        global choice
        choice = int(input("Enter the scenairo number: "))
        while not (choice == 1 or choice == 2 or choice == 3):
            choice = int(input("Please enter 1, 2, or 3: "))
    except ValueError:
        print("Please enter a number")
        get_scenario()

# 2 inputs 1 output
def scenario_one():
    try:
        speed = float(input("What is the speed of the cannonball (m/s)?"))
        height = float(input("What is the height of the cannon above the water (m)?"))
        time = ((2 * height) / gravity) ** 0.5
        hor_speed, ver_speed = speed_vectors(speed, 0)
        distance = hor_speed * time
        print("It takes " + str(time) +"s for the cannonball to fall to the waterline.")
        print("The distance between the cannonball and the boat is " + str(distance) + "m.")
    except ValueError:
        print("Please enter a number.")
        scenario_one()

# 2 inputs 4 outputs
def scenario_two():
    speed = float(input("What is the speed of the cannonball (m/s)?"))
    angle = float(input("What is the angle of the canon along the the horizontial in degrees?"))
    hor_speed, ver_speed = speed_vectors(speed, angle)
    time = 2 * ver_speed / gravity
    distance = hor_speed * time
    print("Horizontal speed: " + str(hor_speed))
    print("Vertical speed: " + str(ver_speed))
    print("Time in the air: " + str(time))
    print("Horizontal distance traveled: " + str(distance))

#
def scenario_three():
    pass

# 2 inputs 2 outputs
def speed_vectors(speed, angle):
    hor_speed = speed * cos(radians(angle))
    ver_speed = speed * sin(radians(angle))
    return hor_speed, ver_speed

operator = intro()
if operator == 1:
    scenario_one()
elif operator == 2:
    scenario_two()
else:
    scenario_three()
