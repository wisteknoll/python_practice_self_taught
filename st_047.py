class Judge():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def judge(self, x, y):
        return self.x is self.y


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def area(self):
        return self.width * self.length

re_1 = Rectangle(10, 20)
rectangle_1 = re_1
re_2 = Rectangle(20, 10)

print(re_1 is rectangle_1)
print(re_1 is re_2)
print(rectangle_1 is re_2)

print("---------")

def compare(obj1, obj2):
    return obj1 is obj2

print(compare(re_1, rectangle_1))
print(compare(re_1, re_2))
print(compare(re_2, rectangle_1))

print("---------")

J_1 = Judge(re_1, re_2)
print(J_1.judge(re_1, re_2))

J_2 = Judge(re_1, rectangle_1)
print(J_2.judge(re_1, rectangle_1))
print(J_2.judge("banana", "tomato"))
print(J_2.judge("tomato", "tomato"))
print(J_2.judge(12, 14))

"""
a = "apple"
b = a
c = "banana"

print(Judge.judge(a, b, c))
"""

"""
re_1 = Rectangle(10, 20)
rectangle_1 = re_1

print(Judge.judge(re_1, rectangle_1))

re_2 = Rectangle(20, 10)

print(Judge(re_1, re_2))
"""    
