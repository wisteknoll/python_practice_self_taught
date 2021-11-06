class Shape():
    def __init__(self):
        pass

    def who_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(Shape):
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    
re = Rectangle(10, 25)
sq = Square(12)

re.who_am_i()
sq.who_am_i()



