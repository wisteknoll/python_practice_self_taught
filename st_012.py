def f01(a):
    return int(a) // 2

def f02(x):
    return int(x) * 4

value = input("value=")

result01 = f01(value)
result02 = f02(result01)

print("result01=" + str(result01))
print("result02=" + str(result02))
