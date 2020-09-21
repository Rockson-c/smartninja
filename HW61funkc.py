def football_p_enter(FootballPlayer):
    print("Enter football player's data!")

    first_name = input("Enter player's first name: ").capitalize()
    last_name = input("Enter player's last name: ").capitalize()
    height_cm = input("Enter player's height in cm: ")
    weight_kg = input("Enter player's weight in kg: ")
    goals = input("Enter the number of player's goals: ")
    yellow_cards = input("Enter the number of player's yellow cards: ")
    red_cards = input("Enter the number of player's red cards: ")

    new_player = FootballPlayer(first_name=first_name, last_name=last_name, height_cm=float(height_cm),
                                weight_kg=float(weight_kg), goals=int(goals), yellow_cards=int(yellow_cards),
                                red_cards=int(red_cards))

    with open("football_players.txt", "w") as football_file:
        football_file.write(str(new_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))


def basketball_p_enter(BasketballPlayer):
    print("Enter Basketball player's data!")

    first_name = input("Enter player's first name: ").capitalize()
    last_name = input("Enter player's last name: ").capitalize()
    height_cm = input("Enter player's height in cm: ")
    weight_kg = input("Enter player's weight in kg: ")
    points_avg = input("Enter the number of player's average points: ")
    rebounds_avg = input("Enter the number of player's average rebounds: ")
    assists_avg = input("Enter the number of player's average assists: ")

    new_player = BasketballPlayer(first_name=first_name, last_name=last_name, height_cm=float(height_cm),
                                  weight_kg=float(weight_kg), points=float(points_avg), rebounds=float(rebounds_avg),
                                  assists=float(assists_avg))

    with open("basketball_players.txt", "w") as basketball_file:
        basketball_file.write(str(new_player.__dict__))

    print("Player successfully entered!")
    print("Player's data: {0}".format(new_player.__dict__))
