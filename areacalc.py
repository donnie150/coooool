print("1=Rectangle 2=Triangle 3=Circle")
userinput = input()
userinput = int(userinput)

if userinput == 1:
    print("Enter base length")

    base = input()
    base = float(base)

    print("Enter height")

    height = input()
    height = float(height)

    both = float(base) * float(height)
    print("The area is " + str(both))
if userinput == 2:
    print("enter base height")

    base = input()
    base = int(base)

    print("Enter Height")

    height = input()
    height = int(height)

    both = .5 * base * height
    boht = int(both)
    print("The area is " + str(both))

if userinput == 3:
    print("Enter Radius")

    radius = input()
    radius = int(radius)
    both = 3.14159265359 * radius ** 2

    print(" Your area is " + str(both))


