class Square():
    def __init__(self, s1):
        self.s1 = s1

    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self, s1):
        self.s1 = int(input("s1="))

sq = Square(10)
print(sq.s1)
print(sq.calculate_perimeter())

sq.change_size(20)
print(sq.s1)
print(sq.calculate_perimeter())
