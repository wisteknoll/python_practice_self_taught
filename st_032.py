import csv

"""
with open("f0928.csv", "w", newline="") as f:
          w = csv.writer(f, delimiter=",")
          w.writerow(["one", "two", "three"])
          w.writerow(["four", "five", "six"])
"""

"""
with open("f09282.csv", "w") as f:
          w = csv.writer(f, delimiter=",")
          w.writerow(["one", "two", "three"])
          w.writerow(["four", "five", "six"])
"""

"""
with open("f0928.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
#        print(",".join(row))
        print(row)
"""

"""
#a = open("f09272.txt", "r", encoding="utf-8")
a = open("f09272.txt", "r")
#a.read()
print(a.read())
a.close()
a = open("f09272.txt", "r")
print(a.read())
a.close()
"""

"""
with open("f0927.txt", "r") as f:
    print(f.read())
with open("f0927.txt", "r") as f:
    print(f.read())
"""

r_list = []

with open("f0927.txt", "r") as f:
#    print(f.read())
    r_list.append(f.read())
print(r_list)

with open("f09272.txt", "r") as f:
    r_list.append(f.read())
#    print(f.read())
print(r_list)

with open("f09273.txt", "r") as f:
    r_list.append(f.read())
print(r_list)

st = open("f0928.csv", "r")
print(st.read())
st.close()

#a = open("f0928.csv", "r")
#r_list.append(a.read())
#a.close()
#print(r_list)

b = open("f0928.csv", "r")
c = csv.reader(b, delimiter=",")
for row in c:
    r_list.append(",".join(row))
print(r_list)
print(len(r_list))











