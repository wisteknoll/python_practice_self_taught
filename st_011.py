def add_f(x, y, z, a=10, b=7):
    print("x=" + str(x))
    print("y=" + str(y))
    print("z=" + str(z))
    print("a=" + str(a))
    print("b=" + str(b))
    sum1 = int(x) + int(y) + int(z)
    print("x+y+z=" + str(sum1))
    sum2 = sum1 + a + b
    print("x+y+z+a+b=" + str(sum2))

xx = input("x=")
yy = input("y=")
zz = input("z=")
add_f(xx, yy, zz)
add_f(xx, yy, zz, 100, 200)

