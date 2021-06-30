from shape import Shape
import helper

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.__length = length

    def area(self):
        return self.__length ** 2

    def perimeter(self):
        return 4 * self.__length

    def answer_check(self, a, p):
        if self.area() == a:
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1
        if self.perimeter() == p:
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1
