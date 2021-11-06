def f_mojiflo(x):
    try:
        x = float(x)
    except ValueError:
        print("cannnot input str.")
    
#    return x

a = input("mojiretsu=")
b = f_mojiflo(a)
print(b)
