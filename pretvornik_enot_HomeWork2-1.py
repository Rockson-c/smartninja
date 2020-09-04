print("Dobrodošli v programu, ki pretvarja med enotami.")

while True:
    print("")
    print("Katere enote želite pretvoriti?")
    vnos_enot = input("Vpiši: km, milje, cm, inch, kg, pound: ")


    if vnos_enot == ("km"):

        while True:
            km = float(input("Vnesi kilometre: "))
            milje = km*0.62137119
            print(f"{km} km je enako {milje} milj")

            odgovor = input("Ali želite nadaljevati? ")
            if odgovor == "ne":
                   break
            elif odgovor == "no":
               break

            elif odgovor == "n":
               break

    if vnos_enot == ("milje"):

        while True:
            milje = float(input("Vnesi milje: "))
            km = milje * 1.6093449
            print(f"{milje} milj je enako {km} km")

            odgovor = input("Ali želite nadaljevati? ")
            if odgovor == "ne":
                break
            elif odgovor == "no":
                break

            elif odgovor == "n":
                break


    elif vnos_enot == ("cm"):

        while True:
            cm = float(input("Vnesi centimetre: "))
            inch = cm*0.39370079
            print(f"{cm} cm je enako {inch} inchov")

            odgovor = input("Ali želite nadaljevati? ")
            if odgovor == "ne":
                   break

            elif odgovor == "no":
               break

            elif odgovor == "n":
               break

    elif vnos_enot == ("inch"):

        while True:
            inch = float(input("Vnesi inche: "))
            cm = inch*2.54
            print(f"{inch} inchov je enako {cm} cm")

            odgovor = input("Ali želite nadaljevati? ")
            if odgovor == "ne":
                   break

            elif odgovor == "no":
               break

            elif odgovor == "n":
               break


    elif vnos_enot == ("kg"):

        while True:
            kg = float(input("Vnesi kilograme: "))
            pound = kg * 2.20462262
            print(f"{kg} kg je enako {pound} poundov")

            odgovor = input("Ali želite nadaljevati? ")
            if odgovor == "ne":
                break

            elif odgovor == "no":
                break

            elif odgovor == "n":
                break

    elif vnos_enot == ("pound"):

        while True:
            pound = float(input("Vnesi pounde: "))
            kg = pound * 0.45359237
            print(f"{pound} poundov je enako {kg} kg")

            odgovor = input("Ali želite nadaljevati? ")
            if odgovor == "ne":
                break

            elif odgovor == "no":
                break

            elif odgovor == "n":
                break

    else:
        print("Ne razumem.")


    restart = input("Restart? ")
    if restart== "ne":
        break

    elif restart == "no":
        break

    elif restart == "n":
        break

print("")
print("Nasvidenje!")