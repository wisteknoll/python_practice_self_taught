"""
class Square:
    pass

print(Square)
"""

"""
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))


my_rectangle = Rectangle(10, 24)
my_rectangle.print_size()
"""

"""
class Rectangle:
    recs = []
    
    def __init__(self, w, l):
        self.width = w
        self.len = l
        self.recs.append((self.width, self.len))

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)
"""

"""
class Lion:
    def __init__(self, name):
        self.name = name

#overwrite__repr__ method
    def __repr__(self):
        return self.name


lion = Lion("Dilbert")
print(lion)
"""

"""
class AlwaysPositive:
    def __init__(self, number):
        self.n = number

    def __add__(self, other):
        return abs(self.n + other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)
"""

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)


another_bob = Person()
print(bob is another_bob)

print("----------")

x = 10
if x is None:
    print("x は None :(")
else:
    print("x は None じゃない")

x = None
if x is None:
    print("x は None ")
else:
    print("x は None じゃない :(")







        






    
