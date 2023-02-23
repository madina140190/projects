import math
print("ax^2+bx+c=0")
try:
    a = input("enter value of a:")
    b = input("enter value of b:")
    c = input ("enter value of c:")
    a = float(a)
    b = float(b)
    c = float(c)

    if a == 0:
        print("a cannot be equal 0")
    else:
        d = float(b * b - 4 * a * c)
        if d == 0:
            x = float(-b / 2 * a)
            print("x =", x)
        elif d > 0:
            x1 = float((-b + math.sqrt(d)) / 2 * a)
            x2 = float((-b - math.sqrt(d)) / 2 * a)
            print("x1 =", x1)
            print("x2 =", x2)
        else:
            print("x cannot be found")
except ValueError:
    print("Error occurred")
