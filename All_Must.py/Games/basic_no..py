import random

print("Hello, Welcome to no. Guessing Game enter no. 1 to 10")

# variables
i = int(input("Enter your number: "))
a = 3
b = 0
o = False

no = random.randint(1, 10)

while b != a and o == False:

    if i >= 11 or i < 1:
        print("out of range")
        i = int(input("Enter your number: "))

    elif i != no:
        b += 1

        if b == a:
            print("You Lose!")
            o = True
        else:
            i = int(input("Enter your number: "))

    else:
        print("You Win!")
        o = True