def total_participants_line(runners):
    print(f"The total number of participants was {len(runners)}")

def participants_sex_line(runners):
    print(f"The total of male runners was {runners['Male']} and female runners was {runners['Female']}")

def general_winner_line(runner):
    print("The General winner is:" )
    print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format("ID"
                                                                ,"Last Name"
                                                                ,"Second Last Name"
                                                                ,"First Name"
                                                                ,"Second Name"
                                                                ,"Sex"
                                                                ,"Age"
                                                                ,"Time"
                                                                ))
    if runner:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runner['id'],
                                                    runner['firstLastName'],
                                                    runner['secondLastName'],
                                                    runner['firstName'],
                                                    runner['initialSecondName'],
                                                    runner['sex'],
                                                    runner['age'],
                                                    str(runner['time'])))

def histogram_age_line(runners):
    print(f"Juniors ({round(runners['juniors'])}): | ",end="")
    for i in range(round(runners['juniors'])):
        print("*", end="")
    print()
    print(f"Seniors ({round(runners['seniors'])}): | ",end="")
    for i in range(round(runners['seniors'])):
        print("*", end="")
    print()
    print(f"Masters ({round(runners['masters'])}): | ",end="")
    for i in range(round(runners['masters'])):
        print("*", end="")
    print()

def average_age_sex_line(runners):
    print(runners)
