import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
     ["Titanic", "The Revenant", "Inception"],
     ["Training Day", "Man on Fire", "Flight"]
     ]

with open("movie.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)


with open("movie.csv", "r") as csvfile:
    r = csv.reader(csvfile, delimiter=",")
    for row in r:
        print(",".join(row))

