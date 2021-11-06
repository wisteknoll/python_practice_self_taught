import os
import csv

a = [["Top Gun", "Risky Business", "Minority Report"],
     ["Titanic", "The Revenant", "Inception"],
     ["Training Day", "Man on Fire", "Flight"]
     ]

with open("cinema_list.csv", "w") as c:
    cc = csv.writer(c, delimiter=",")
    for row in a:
        cc.writerow(row)

with open("cinema_list.csv", "r") as d:
    e = csv.reader(d, delimiter=",")
    for row in e:
        print(",".join(row))



