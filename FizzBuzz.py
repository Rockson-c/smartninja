print("")
print("Welcome to FizzBuzz!")
print("")
while True:
    number = int(input("Please choose your number, 1 - 100: "))
    print("")
    while number > int(100):
        print("oops")
        break

    else:
        for x in range(1, number + 1):

            if x % 3 == 0 and x % 5 == 0:
                        print("FizzBuzz")

            elif x % 3 == 0:
                print("fizz")

            elif x % 5 == 0:
                print("buzz")

            else:
                print(x)

    print("")
    nadaljuj = input("Nadaljuj? ")
    print("")
    if nadaljuj == "ne":
        break
        

    elif nadaljuj == "no":
        break

    elif nadaljuj == "n":
        break