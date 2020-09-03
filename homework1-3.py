print("Welcome to basic CALCULATOR! Input numbers and math operations.")
print()

x = float(input("First number: "))
mathoperation = input("Choose + or - or * or /: ")
y = float(input("Second number: "))

if mathoperation == "+":
    print(x + y)

elif mathoperation == "-":
    print(x-y)

elif mathoperation == "*":
    print(x*y)

elif mathoperation == "/":
    print(x/y)

else:
    print("I don't understand")