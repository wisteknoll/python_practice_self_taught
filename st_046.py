class Square():
    def __init__(self, s1):
        self.s1 = s1

    def square_print(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)


sq_1 = Square(29)
print(sq_1.s1)
print(sq_1.square_print())
print(sq_1)


class Sq_Repr(Square):
    def __repr__(self):
        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)
        
sq_2 = Sq_Repr(48)
print(sq_2.s1)
print(sq_2.square_print())
print(sq_2)
