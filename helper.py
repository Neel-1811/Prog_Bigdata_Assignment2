import random

user_score = {}
current_user = "user"


def randomshape():
    shape_list = ['Square', 'Rectangle', 'Circle', 'Triangle']
    return random.choice(shape_list)


def randomdimension():
    n = random.randint(1, 100)
    return n


def area_value_validator():
    flag1 = True
    while flag1:
        try:
            area = float(input("Enter area:\n"))
            flag1 = False
            return area
        except:
            print("Please enter integer or float value")


def perimeter_value_validator():
    flag2 = True
    while flag2:
        try:
            perimeter = float(input("Enter perimeter:\n"))
            flag2 = False
            return perimeter
        except:
            print("Please enter integer or float value")