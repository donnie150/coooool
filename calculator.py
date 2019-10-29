def Calc():
    num1 = input("Enter first number\n")
    num1 = float(num1)
    num2 = input("Enter operation\n")
    num3 = input("Enter second number\n")
    num3 = float(num3)

    if num2 == "-":
        both = num1-num3
    if num2 == "+":
        both = num1+num3
    if num2 == "*" or "x":
        both = num1*num3
    if num2 == "/":
        both = num1/num3
    print("Your anwser is " + str(both))
