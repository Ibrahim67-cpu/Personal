# Tuple in Python
friends = ("Kevin", "Karen", "Jim")
print(friends[1:])

#List in Python
Alphabet = ["A", "B", "C", "D", "E"]
print(Alphabet)

#List Functions
lucky_numbers = [1, 2, 3, 4, 5]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends2 = friends.copy()
print(friends2)

# Functions
def sayhi(name, age):
    print("Hello " + name + ", you are " + str(age))
sayhi("Ibrahim", 9)

#Result statements
def cube(num):
    return num*num*num
result = cube(2)
print(result)

#while loop
i = int (input ("enter a no. lower than 9:"))
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

#While Loops
i = int (input ("enter a no. lower than 9:"))
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

#expo9nent function
def a(bn, pn):
    result = 1
    for index in range(pn):
        result = result * bn
    return result

print(a(2, 3))




