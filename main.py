import helper
from square import Square
from rectangle import Rectangle
from circle import Circle
from triangle import Triangle


def askmeasure(shape):
    if shape == "Square":
        l = helper.randomdimension()
        print("length:{}\n".format(l))
        s_area = helper.area_value_validator()
        s_peri = helper.perimeter_value_validator()
        square1 = Square(l)
        square1.answer_check(s_area, s_peri)

    elif shape == "Rectangle":
        l = helper.randomdimension()
        w = helper.randomdimension()
        print("length:{} width:{}\n".format(l, w))
        r_area = helper.area_value_validator()
        r_peri = helper.perimeter_value_validator()
        rect = Rectangle(l, w)
        rect.answer_check(r_area, r_peri)

    elif shape == "Circle":
        r = helper.randomdimension()
        print("radius:{}\n".format(r))
        c_area = helper.area_value_validator()
        c_peri = helper.perimeter_value_validator()
        circ = Circle(r)
        circ.answer_check(c_area, c_peri)

    elif shape == "Triangle":
        s = helper.randomdimension()
        print("side:{}\n".format(s))
        t_area = helper.area_value_validator()
        t_peri = helper.perimeter_value_validator()
        tri = Triangle(s)
        tri.answer_check(t_area, t_peri)


def total_shape():
    global number
    flag4 = True
    while flag4:
        try:
            number = int(input("Enter number of shapes you want to play with:\n"))
            flag4 = False
        except:
            print("Please enter integer input.")

    while number:
        shape = helper.randomshape()
        print("Shape:", shape)
        askmeasure(shape)
        number = number - 1

    print("Your score:", helper.user_score[helper.current_user])

    flag6 = True
    while flag6:
        choice = input("Do you want to play further 'y' for YES and 'n' for NO\n")
        if choice == "y":
            total_shape()
            flag6 = False
        elif choice == "n":
            option()
            flag6 = False
        else:
            print("please choose 'y' or 'n'")


def registration():
    username = input("Enter Your Name:\n")

    if not helper.user_score.keys().__contains__(username):
        print("{}, Your Registration is successful.".format(username))
        helper.user_score[username] = 0
        helper.current_user = username
        total_shape()
    else:
        print("User already exist.Please enter another username")
        registration()


def option():
    print("***********************************")
    print("**** Select From Below Option *****")
    print("***********************************")
    print("(1) User Registration\n(2) Show Score\n(3) Quit")

    flag3 = True
    while flag3:
        user_option = input("Enter Your Choice:\n")
        if user_option == "1":
            registration()
            flag3 = False

        elif user_option == "2":
            if len(helper.user_score.keys()) > 0:
                print("-----SCORE BOARD-------")
                for a in helper.user_score.keys():
                    print("-    {}:{}      ".format(a, helper.user_score[a]))
                print("-----------------------\n")
            else:
                print("-----SCORE BOARD--------")
                print("  No Data Available.  ")
                print("------------------------\n")

            option()
            flag3 = False

        elif user_option == "3":
            print("Thank You For Playing The Game.Hope You Enjoyed it.")
            flag3 = False

        else:
            print("please choose from (1) (2) (3).")


if __name__ == "__main__":
    option()
