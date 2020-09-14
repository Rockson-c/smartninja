# Kako odstraniti mikrosekunde iz timedate?
# Kako obrniti datum, ura/dan/mesec/leto?

import random
import json
import datetime
import operator

secret = random.randint(1, 30)
attempts = 0

print("")
print("Welcome to guess the number game! Try to beat the top score.")
print("")

with open("score_list_homework.txt", "r") as score_file:
    file_content = score_file.read()
    score_list = json.loads(file_content)
    score_list.sort(key=operator.itemgetter('attempts'))

    print("Top Scores: ")
    for score_dict in score_list[:3]:
        #print(str(score_dict['Name']) + ", " + str(score_dict['attempts']) + " attempts, date: " + str(score_dict['date']) + " number: " + str(score_dict['snumber']))
        print(f"{score_dict['Name']}, "
              f"{score_dict['attempts']} attempts, "
              f"date {score_dict['date']}, "
              f"number: {score_dict['snumber']} "
              f"/wrong guesses: {score_dict['wrong']}")

wrong_guesses = []

while True:
    try:
        print("")
        guess = int(input("Guess the number between 1 and 30: "))
        attempts += 1

    except ValueError:
        attempts += 1
        print(f"Error. {attempts}")

    else:

        if guess == secret:
            print("")
            print(f"Congratulations its number {secret}! :)")
            print(f"You guessed the number in {attempts} attempts.")
            print(f"Wrong guesses: {wrong_guesses}")
            print("")
            name = input("What is your name? ")
            score_list.append({"Name": name,
                               "attempts": attempts,
                               "date": str(datetime.datetime.now()),
                               "snumber": secret,
                               "wrong": wrong_guesses})

            with open("score_list_homework.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

            break
        elif guess > secret:
            print("No, try lower.")
            wrong_guesses.append(guess)
        elif guess < secret:
            print("No, try higher.")
            wrong_guesses.append(guess)
