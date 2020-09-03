user_name = input("Please enter your name: ")
print("Hello " + user_name +"!")

mood = input("What mood are you in? ")

if mood == "happy":
    print("It is great to see you happy " + user_name +"!")

elif mood == "sad":
    print("Oh no. So sad.")

elif mood == "nervous":
    print(user_name + " take a deep breath 3 times to relax a bit.")

elif mood == "excited":
    print("Yay!")

elif mood == "relaxed":
    print("Nice to hear that " + user_name + ".")

else:
    print("I don't recognize this mood.")