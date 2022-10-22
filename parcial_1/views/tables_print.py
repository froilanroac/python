
from cProfile import run
from unittest import runner


def all_runners_table(runners):
    print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format("ID"
                                                                ,"Last Name"
                                                                ,"Second Last Name"
                                                                ,"First Name"
                                                                ,"Second Name"
                                                                ,"Sex"
                                                                ,"Age"
                                                                ,"Time"
                                                                ))
    for runner in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runner['id'],
                                                    runner['firstLastName'],
                                                    runner['secondLastName'],
                                                    runner['firstName'],
                                                    runner['initialSecondName'],
                                                    runner['sex'],
                                                    runner['age'],
                                                    str(runner['time'])))

def participants_age_table(runners):
    print ("{:<10} {:<10}".format("Age group","Number of participants"))
    for key, value in runners.items():
        print ("{:<10} {:<12}".format(key,value))

def winners_age_table(runners):
    print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format("ID"
                                                                ,"Last Name"
                                                                ,"Second Last Name"
                                                                ,"First Name"
                                                                ,"Second Name"
                                                                ,"Sex"
                                                                ,"Age"
                                                                ,"Time"
                                                                ))

    if "Juniors" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Juniors']['id'],
                                                    runners['Juniors']['firstLastName'],
                                                    runners['Juniors']['secondLastName'],
                                                    runners['Juniors']['firstName'],
                                                    runners['Juniors']['initialSecondName'],
                                                    runners['Juniors']['sex'],
                                                    runners['Juniors']['age'],
                                                    str(runners['Juniors']['time'])))
    if "Seniors" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Seniors']['id'],
                                                    runners['Seniors']['firstLastName'],
                                                    runners['Seniors']['secondLastName'],
                                                    runners['Seniors']['firstName'],
                                                    runners['Seniors']['initialSecondName'],
                                                    runners['Seniors']['sex'],
                                                    runners['Seniors']['age'],
                                                    str(runners['Seniors']['time'])))
    if "Masters" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Masters']['id'],
                                                    runners['Masters']['firstLastName'],
                                                    runners['Masters']['secondLastName'],
                                                    runners['Masters']['firstName'],
                                                    runners['Masters']['initialSecondName'],
                                                    runners['Masters']['sex'],
                                                    runners['Masters']['age'],
                                                    str(runners['Masters']['time'])))
def winners_age_sex_table(runners):
    print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format("ID"
                                                                ,"Last Name"
                                                                ,"Second Last Name"
                                                                ,"First Name"
                                                                ,"Second Name"
                                                                ,"Sex"
                                                                ,"Age"
                                                                ,"Time"
                                                                ))
    print('Juniors_Male')
    if "Juniors_Male" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Juniors_Male']['id'],
                                                    runners['Juniors_Male']['firstLastName'],
                                                    runners['Juniors_Male']['secondLastName'],
                                                    runners['Juniors_Male']['firstName'],
                                                    runners['Juniors_Male']['initialSecondName'],
                                                    runners['Juniors_Male']['sex'],
                                                    runners['Juniors_Male']['age'],
                                                    str(runners['Juniors_Male']['time'])))
    print('Juniors_Female')
    if "Juniors_Female" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Juniors_Female']['id'],
                                                    runners['Juniors_Female']['firstLastName'],
                                                    runners['Juniors_Female']['secondLastName'],
                                                    runners['Juniors_Female']['firstName'],
                                                    runners['Juniors_Female']['initialSecondName'],
                                                    runners['Juniors_Female']['sex'],
                                                    runners['Juniors_Female']['age'],
                                                    str(runners['Juniors_Female']['time'])))
    print('Seniors_Male')
    if "Seniors_Male" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Seniors_Male']['id'],
                                                    runners['Seniors_Male']['firstLastName'],
                                                    runners['Seniors_Male']['secondLastName'],
                                                    runners['Seniors_Male']['firstName'],
                                                    runners['Seniors_Male']['initialSecondName'],
                                                    runners['Seniors_Male']['sex'],
                                                    runners['Seniors_Male']['age'],
                                                    str(runners['Seniors_Male']['time'])))
    print('Seniors_Female')
    if "Seniors_Female" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Seniors_Female']['id'],
                                                    runners['Seniors_Female']['firstLastName'],
                                                    runners['Seniors_Female']['secondLastName'],
                                                    runners['Seniors_Female']['firstName'],
                                                    runners['Seniors_Female']['initialSecondName'],
                                                    runners['Seniors_Female']['sex'],
                                                    runners['Seniors_Female']['age'],
                                                    str(runners['Seniors_Female']['time'])))
    print('Masters_Male')
    if "Masters_Male" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Masters_Male']['id'],
                                                    runners['Masters_Male']['firstLastName'],
                                                    runners['Masters_Male']['secondLastName'],
                                                    runners['Masters_Male']['firstName'],
                                                    runners['Masters_Male']['initialSecondName'],
                                                    runners['Masters_Male']['sex'],
                                                    runners['Masters_Male']['age'],
                                                    str(runners['Masters_Male']['time'])))
    print('Masters_Female')
    if "Masters_Female" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['Masters_Female']['id'],
                                                    runners['Masters_Female']['firstLastName'],
                                                    runners['Masters_Female']['secondLastName'],
                                                    runners['Masters_Female']['firstName'],
                                                    runners['Masters_Female']['initialSecondName'],
                                                    runners['Masters_Female']['sex'],
                                                    runners['Masters_Female']['age'],
                                                    str(runners['Masters_Female']['time'])))
def winners_sex_table(runners):
    print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format("ID"
                                                                ,"Last Name"
                                                                ,"Second Last Name"
                                                                ,"First Name"
                                                                ,"Second Name"
                                                                ,"Sex"
                                                                ,"Age"
                                                                ,"Time"
                                                                ))
    print('Male')
    if "male" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['male']['id'],
                                                    runners['male']['firstLastName'],
                                                    runners['male']['secondLastName'],
                                                    runners['male']['firstName'],
                                                    runners['male']['initialSecondName'],
                                                    runners['male']['sex'],
                                                    runners['male']['age'],
                                                    str(runners['male']['time'])))
    print('female')
    if "female" in runners:
        print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format(
                                                    runners['female']['id'],
                                                    runners['female']['firstLastName'],
                                                    runners['female']['secondLastName'],
                                                    runners['female']['firstName'],
                                                    runners['female']['initialSecondName'],
                                                    runners['female']['sex'],
                                                    runners['female']['age'],
                                                    str(runners['female']['time'])))
def average_age_sex_table(runners):
    print ("{:<15} {:<15} {:<15} ".format("Age","Sex", "Average"))
    if "juniors_male" in runners:
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Juniors Male"
                                                                    ,"M"
                                                                    ,runners['juniors_male']))
    if "juniors_female" in runners:
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Juniors Female"
                                                                    ,"F"
                                                                    ,runners['juniors_female']))
    if "seniors_male" in runners:
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Seniors Male"
                                                                    ,"M"
                                                                    ,runners['seniors_male']))
    if "seniors_female" in runners:
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Seniors Female"
                                                                    ,"F"
                                                                    ,runners['seniors_female']))
    if "masters_male" in runners:
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Masters Male"
                                                                    ,"M"
                                                                    ,runners['masters_male']))
    if "masters_female" in runners:
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Masters Female"
                                                                    ,"F"
                                                                    ,runners['masters_female']))