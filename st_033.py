import os
import datetime

a = input("今日の天気は？：")
with open("tenki_log.txt", "w", encoding="utf-8") as f:
    f.write(a)

with open("tenki_log.txt", "r", encoding="utf-8") as r:
    print(datetime.date.today(), r.read())
