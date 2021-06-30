from shape import Shape
import math
import helper


class Triangle(Shape):
    def __init__(self, side):
        super().__init__()
        self.__side = side

    def area(self):
        return (math.sqrt(3) * (self.__side ** 2)) / 4

    def perimeter(self):
        return 3 * self.__side

    def answer_check(self, a, p):
        if math.isclose(self.area(), a, rel_tol=0.01):
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1
        if math.isclose(self.perimeter(), p, rel_tol=0.01):
            helper.user_score[helper.current_user] = helper.user_score[helper.current_user] + 1
