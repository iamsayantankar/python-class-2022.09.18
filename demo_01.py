# Get 4 user input and show largest, 2nd Largest and smallest number


a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))

max01 = max(a, b, c)
min01 = min(a, b, c)

mid01 = a + b + c - max01 - min01

print("max number is: ", max01)
print("min number is: ", min01)
print("mid number is: ", mid01)

if (a > b) and (a > c):
    print("max number is: ", a)
    if b > c:
        print("min number is: ", c)
        print("mid number is: ", b)
    else:
        print("min number is: ", b)
        print("mid number is: ", c)
if (b > a) and (b > c):
    print("max number is: ", b)
    if c > a:
        print("min number is: ", a)
        print("mid number is: ", c)
    else:
        print("min number is: ", c)
        print("mid number is: ", a)
if (c > b) and (c > a):
    print("max number is: ", )
    if b > a:
        print("min number is: ", a)
        print("mid number is: ", b)
    else:
        print("min number is: ", b)
        print("mid number is: ", a)
