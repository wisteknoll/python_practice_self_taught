shows = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for show in shows:
    print(show)

print("----------")

a = []
a.append(25)
print(a)
a.insert(0, "kome")
print(a)

#list1 = [2, 3, 4, 5]

#list1 = []

#list1.append(6)
#print(list1)
#list1.append(7)
#print(list1)
#list1.append(1)
#print(list1)

print("----------")

for i in range(25,51):
    print(i)

print("----------")


for index, show in enumerate(shows):
    print(index)
    print(show)
    
print("----------")

print("kome" in shows)
print("The Walking Dead" in shows)

ans = [13, 26, 39, 52]
print(type(ans[0]))

print("----------")

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Guess a number or type q to quit.")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("please type a number or q to quit.")
        continue
    if answer in numbers:
        print("You guessed correctly!")
    else:
        print("You guessed incorrectly!")


    



