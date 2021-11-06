answer = input("What is your favorite color ?")
with open("fav_color.txt", "w") as f:
    f.write(answer)


with open("fav_color.txt", "r") as r:
    print(r.read())

