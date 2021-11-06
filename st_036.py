class Apple:
    def __init__(self, x, y, z, w):
        self.color = x
        self.weight = y
        self.flavor = z
        self.taste = w
        print("created.")


a = Apple("red", "200", "good", "sweet")
print(a)
#print(Apple.color, Apple.weight, Apple.flavor, Apple.taste)
print(a.color)
print(a.color, a.weight, a.flavor, a.taste)

