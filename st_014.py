list_a = ["bump of chiken", "Judy and Mary", "super fly", "B'z"]
print(list_a)

print("----------")

list_b = [("kawasaki_station", 35.532984, 139.7009903), ("lazona_kawasaki", 35.5330968, 139.6959065), ("grantree", 35.5738232, 139.6603311)]
print(list_b)

print("----------")

dict_c = {"orange":"orange", "apple":"red", "banana":"yellow", "grape":"purple"}
print(dict_c)

print("----------")

key = input("key=")
if key in dict_c:
    print(dict_c[key])
else:
    print("not exist.")
