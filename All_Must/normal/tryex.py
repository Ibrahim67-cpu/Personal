#try & except
try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("Invalid input. Please enter a valid integer.")

