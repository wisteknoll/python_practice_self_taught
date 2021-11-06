class Rider():
    def __init__(self, namae):
        self.namae = namae

class Horse():
    def __init__(self, n, w, r):
        self.name = n
        self.weight = w
        self.rider = r

a_rider = Rider("tanaka")
print(a_rider.namae)
a_horse = Horse("narita", 500, a_rider)
print(a_horse.name)
print(a_horse.weight)
print(a_horse.rider.namae)

#print(a_horse.rider)



