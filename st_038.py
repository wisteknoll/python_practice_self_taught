class Triangle():
    def __init__(self, l, h):
        self.length = l
        self.height = h

    def area(self):
        return self.length * self.height / 2

a,b = map(int, input("input length and height,").split())
print("length= ", a)
print("height= ", b)
#a = int(a)
#b = int(b)
x_triangle = Triangle(a,b)
print("triangle_area = ", x_triangle.area())

