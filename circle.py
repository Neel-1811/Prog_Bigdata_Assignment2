from shape import Shape
import helper
import math


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def area(self):
        return 3.14 * (self.__radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.__radius

    def answer_check(self, a, p):
        if math.isclose(self.area(), a, rel_tol=0.01):
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1
        if math.isclose(self.perimeter(), p, rel_tol=0.01):
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1
