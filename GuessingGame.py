#Guessing Game
secret = "Ibr"
guess = ""
guess_count = 0
guess_limit = 3
out = False

print("Welcome to no. guessing Game!")
print("Hint: It's my nickname")

while guess != secret and not (out):

    if guess_count < guess_limit:
        guess = input("Enter your guess :")
        guess_count += 1

    else:
        out = True

if out:
    print("You Lose!")
    
else:      
    print("You Win!")