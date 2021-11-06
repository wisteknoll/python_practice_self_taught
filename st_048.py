class Item(object):
    def __init__(self, price):
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return self.price < other.price

    def __ne__(self, other):
        return not self.__eq__(other)

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)
    




item1 = Item(100)
item2 = Item(101)

print(item1 < item2)
print("-----------")
print(item1 == item2)
print(item1 == 101)
print(item1 < item2)
print(item1 != item2)
print(item1 <= item2)
print(item1 > item2)
print(item1 >= item2)

