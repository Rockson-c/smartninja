secret = 19

guess = int(input("Find out the secret number! Which number is your choice? "))


if secret == guess :
    print("Congratulations WINNER!")

else:
    print("Your number " + str(guess) + " is WRONG.")