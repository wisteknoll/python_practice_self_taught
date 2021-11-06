def squared(x):
    """
    returns x ** 2.
    :param x: int.
    :return: int x ** 2.
    """
    return x ** 2

print(squared(2))

print("----------")

def print_string(string):
    """
    print string.
    :param string: int.
    :return print(string)
    """
    print(string)

print_string("Testing: 1, 2, 3.")

print("----------")

def add_mult(a, b, c, x=100, z=1000):
    """
    add and multiply.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param z: int.
    :return : a+b+c*x*z. 
    """
    return a + b + c * x * z

result = add_mult(10, 15, 25)
print(result)

print("----------")

def divide(x):
    """
    divide x by 2.
    :param x: int.
    :return: x / 2
    """
    return x / 2

def multiply(x):
    """
    multiple x * 4
    :param x: int.
    :return: x * 4.
    """
    return x * 4

y = divide(4)
z = multiply(y)
print(z)

print("----------")

def convert(string):
    """
    returns variable converted float.
    :param string: int. if not, exception operation will do.
    :return: float(string). if not, print error message.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)
d = convert("reigai_hassei")
print(d)

