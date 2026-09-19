#Calculator Game

num1 = float(input("Enter your first no.: "))
op = input("Enter operator: ")
num2 = float(input ("Enter your second no. :"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")
