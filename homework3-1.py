with open("homework3-1.csv", 'r') as homework_file:
    content = homework_file.readlines()

    for row in content:
        row_data = row.split(",")
        print(f"{row_data[0]} is {row_data[1]} years old and {row_data[2]}.")
