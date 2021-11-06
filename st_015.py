fav_musicans = ["Jay Z", "Adventure Club", "John Lennon"]
print(fav_musicans)

print("----------")

locations = [(40.7128, 74.0059), (31.0461, 34,8516), (8.3405, 115.0920)]
print(locations)

print("----------")

me = {
    "height":"6",
    "fav_color":"red",
    "fav_author":"Orwell"
    }
print(me)

print("----------")

answer = input("Type height, fav_color or fav_author : ")
if answer in me:
    result = me[answer]
    print(result)
    
print("----------")

songs = {"John Lennon":"stand by Me",
         "Kanye West":"Homecoming",
         "Swedish House Mafia":"Don't You Worry Child"
         }
print(songs)
