print("What would you like to add?")
print("1 - ADD")
print("2 - MULTIPLY")
print("3 - SUBTRACT")
print("4 - DIVIDE")

number = input()


if number == "1":
    num1 = input("First number?")
    num2 = input("Second number?")
    print("Hello Brent your answer is...." + str(int(num1) + int(num2)))
elif number == "2":
    num1 = input("First number?")
    num2 = input("Second number?")
    print("Hello Brent your answer is...." + str(int(num1) * int(num2)))
elif number == "3":
    num1 = input("First number?")
    num2 = input("Second number?")
    print("Hello Brent your answer is...." + str(int(num1) - int(num2)))
elif number == "4":
    num1 = input("First number?")
    num2 = input("Second number?")
    print("Hello Brent your answer is...." + str(int(num1) / int(num2)))
else:
    print("This is not one of the choices")

