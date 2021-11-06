import csv

a = [["トップ　ガン", "リスキー　ビジネス", "マイノリティ　リポート"],
     ["タイタニック", "ザ　レヴァナント", "インセプション"],
     ["トレーニング　デイ", "マン　オン　ファイア", "フライト"]
     ]

with open("cinema_list.csv", "w", encoding="utf-8") as c:
    cc = csv.writer(c, delimiter=",")
    for row in a:
        cc.writerow(row)

with open("cinema_list.csv", "r", encoding="utf-8") as d:
    e = csv.reader(d, delimiter=",")
    for row in e:
        print(",".join(row))
