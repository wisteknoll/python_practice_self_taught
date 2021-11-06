import math

"""
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self, radius):
        x = radius ** 2 * math.pi
        print(x)
#        return self.radius ** 2 * math.pi
    
a = Circle(12)
a.area(12)
#print(a.area())
"""

class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * math.pi

r = input("r=")
a_circle = Circle(int(r))
print(a_circle.area())
    
