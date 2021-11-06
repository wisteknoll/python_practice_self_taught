class Square():
    square_list = []

    def __init__(self, w, l):
        self.width = w
        self.length = l
        self.square_list.append((self.width, self.length))


sq_1 = Square(10, 20)
sq_2 = Square(15, 23)
sq_3 = Square(44, 16)

print(Square.square_list)
