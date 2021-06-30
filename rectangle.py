from shape import Shape
import helper


class Rectangle(Shape):
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def perimeter(self):
        return 2 * (self.__length + self.__width)

    def answer_check(self, a, p):
        if self.area() == a:
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1
        if self.perimeter() == p:
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1