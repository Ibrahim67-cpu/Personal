def trans(phrase):
    tran = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            tran = tran + "i"
        else:
            tran = tran + letter
    return tran

print(trans(input("Enter a phrase: ")))