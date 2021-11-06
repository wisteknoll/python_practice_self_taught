class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square(Rectangle):
    pass

ar = Rectangle(10, 20)
print(ar.length)
print(ar.width)
print(ar.calculate_perimeter())

sq = Square(10, 20)
print(sq.length)
print(sq.width)
print(sq.calculate_perimeter())

