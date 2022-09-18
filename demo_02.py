# Get 4 user input and show largest, 2nd Largest and smallest number

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))
c = int(input("Enter the number c: "))
d = int(input("Enter the number d: "))


# Method 01
if (d > b) and (d > c) and (d > a):
    print("Largest number is: ", d)
    if (a > b) and (a > c):
        print("2nd Largest: ", a)
        if b > c:
            print("3rd Largest: ", b)
            print("Smallest: ", c)
        else:
            print("3rd Largest: ", c)
            print("Smallest: ", b)

    if (b > a) and (b > c):
        print("2nd Largest: ", b)
        if c > a:
            print("3rd Largest: ", c)
            print("Smallest: ", a)
        else:
            print("3rd Largest: ", a)
            print("Smallest: ", c)

    if (c > b) and (c > a):
        print("2nd Largest: ", c)
        if b > a:
            print("3rd Largest: ", b)
            print("Smallest: ", a)
        else:
            print("3rd Largest: ", a)
            print("Smallest: ", b)

if (c > b) and (c > d) and (c > a):
    print("Largest number is: ", c)
    if (a > b) and (a > d):
        print("2nd Largest: ", a)
        if b > d:
            print("3rd Largest: ", b)
            print("Smallest: ", d)
        else:
            print("3rd Largest: ", d)
            print("Smallest: ", b)

    if (b > a) and (b > d):
        print("2nd Largest: ", b)
        if a > d:
            print("3rd Largest: ", a)
            print("Smallest: ", d)
        else:
            print("3rd Largest: ", d)
            print("Smallest: ", a)

    if (d > b) and (d > a):
        print("2nd Largest: ", d)
        if b > a:
            print("3rd Largest: ", b)
            print("Smallest: ", a)
        else:
            print("3rd Largest: ", a)
            print("Smallest: ", b)

if (b > d) and (b > c) and (b > a):
    print("Largest number is: ", b)
    if (a > d) and (a > c):
        print("2nd Largest: ", a)
        if d > c:
            print("3rd Largest: ", d)
            print("Smallest: ", c)
        else:
            print("3rd Largest: ", c)
            print("Smallest: ", d)

    if (d > a) and (d > c):
        print("2nd Largest: ", d)
        if a > c:
            print("3rd Largest: ", a)
            print("Smallest: ", c)
        else:
            print("3rd Largest: ", c)
            print("Smallest: ", a)

    if (c > d) and (c > a):
        print("2nd Largest: ", c)
        if a > d:
            print("3rd Largest: ", a)
            print("Smallest: ", d)
        else:
            print("3rd Largest: ", d)
            print("Smallest: ", a)

if (a > b) and (a > c) and (a > d):
    print("Largest number is: ", a)
    if (d > b) and (d > c):
        print("2nd Largest: ", d)
        if b > c:
            print("3rd Largest: ", b)
            print("Smallest: ", c)
        else:
            print("3rd Largest: ", c)
            print("Smallest: ", b)

    if (b > d) and (b > c):
        print("2nd Largest: ", b)
        if d > c:
            print("3rd Largest: ", d)
            print("Smallest: ", c)
        else:
            print("3rd Largest: ", c)
            print("Smallest: ", d)

    if (c > b) and (c > d):
        print("2nd Largest: ", c)
        if d > c:
            print("3rd Largest: ", d)
            print("Smallest: ", c)
        else:
            print("3rd Largest: ", d)
            print("Smallest: ", b)



# Method 02
if (d > b) and (d > c) and (d > a):
    print("Largest number is: ", d)
    if (a > b) and (a > c):
        print("2nd Largest: ", a)

    if (b > a) and (b > c):
        print("2nd Largest: ", b)

    if (c > b) and (c > a):
        print("2nd Largest: ", c)

if (c > b) and (c > d) and (c > a):
    print("Largest number is: ", c)
    if (a > b) and (a > d):
        print("2nd Largest: ", a)

    if (b > a) and (b > d):
        print("2nd Largest: ", b)

    if (d > b) and (d > a):
        print("2nd Largest: ", d)

if (b > d) and (b > c) and (b > a):
    print("Largest number is: ", b)
    if (a > d) and (a > c):
        print("2nd Largest: ", a)

    if (d > a) and (d > c):
        print("2nd Largest: ", d)

    if (c > d) and (c > a):
        print("2nd Largest: ", c)

if (a > b) and (a > c) and (a > d):
    print("Largest number is: ", a)
    if (d > b) and (d > c):
        print("2nd Largest: ", d)

    if (b > d) and (b > c):
        print("2nd Largest: ", b)

    if (c > b) and (c > d):
        print("2nd Largest: ", c)

if (d < b) and (d < c) and (d < a):
    print("Smallest number is: ", d)

if (c < b) and (c < d) and (c < a):
    print("Smallest number is: ", c)

if (b < d) and (b < c) and (b < a):
    print("Smallest number is: ", b)

if (a < b) and (a < c) and (a < d):
    print("Smallest number is: ", a)
