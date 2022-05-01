# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

print("This program will add, subtract, multiply, divide two numbers")
print("or convert one number between Celsius and Fahrenheit.")
mode = input("What operation do you wish to perform? Enter +, -, *, /, C, or F here: ")
if mode == "+":
    num1 = float(input(f"Enter the base number: "))
    num2 = float(input(f"Enter the number you want to add: "))
    print(f"The result of {num1} {mode} {num2} = {num1 + num2}.")
elif mode == "-":
    num1 = float(input(f"Enter the base number: "))
    num2 = float(input(f"Enter the number you want to subtract: "))
    print(f"The result of {num1} {mode} {num2} = {num1 - num2}.")
elif mode == "*":
    num1 = float(input(f"Enter the base number: "))
    num2 = float(input(f"Enter the number to multiply to the base number: "))
    print(f"The result of {num1} {mode} {num2} = {num1 * num2}.")
elif mode == "/":
    num1 = float(input(f"Enter the base number: "))
    num2 = float(input(f"Enter the number to divide from the base number: "))
    print(f"The result of {num1} {mode} {num2} = {num1 / num2}.")
elif mode.upper() == "C":
    num1 = float(input(f"Enter the base number: "))
    print(f"The temperature of {num1}C = {num1 * 9 / 5 + 32}F.")
elif mode.upper() == "F":
    num1 = float(input(f"Enter the base number: "))
    print(f"The temperature of {num1}F = {(num1-32) * 5 / 9}C.")
else:
    print("The program ended because you didn't enter a correct symbol. This will only accept these four + - * /  ")
    raise SystemExit(1)
