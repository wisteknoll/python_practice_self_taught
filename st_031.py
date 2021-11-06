#with open("f0927.txt", "w") as f:
#    f.write("Hi! from python.")

#with open("f0927.txt", "r") as f:
#    print(f.read())

#with open("f0927.txt", "r", encoding="utf-8") as f:
#    print(f.read())

my_list = []

with open("f0927.txt", "r", encoding="utf-8") as f:
    my_list.append(f.read())

print(my_list)
