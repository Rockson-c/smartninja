# Kako v eno od definiranih funkcij vstavit slovarje iz drugih definiranih funkcij in jih zdruziti?
# Kaj spremeniti, da playerje dodane preko 'input' doda v file.txt/class (append) in ne zbrise prejsnjega vnosa?
# Ali je kakšen line za ustavit program - quit?

from HW61funkc import football_p_enter
from HW61funkc import basketball_p_enter

class Player():
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_to_lbs(self):
        pounds = self.weight_kg * 2.20462262
        return pounds


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        super().__init__(first_name=first_name, last_name=last_name,
                         height_cm=height_cm, weight_kg=weight_kg) # dostopam do razreda katerega dedujem
        self.points = points
        self.rebounds = rebounds
        self.assists = assists


class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        super().__init__(first_name=first_name, last_name=last_name, height_cm=height_cm, weight_kg=weight_kg)
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

while True:
    while True:
        borf = input("Enter players data. A) footbal B) basketball >").lower()
        if borf == "a":
            football_p_enter(FootballPlayer)
        elif borf == "b":
            basketball_p_enter(BasketballPlayer)
        else:
            break

    quit = input("ENTER new player or QUIT? ").upper()
    if quit == "Q":
        break
    elif quit == "QUIT":
        break