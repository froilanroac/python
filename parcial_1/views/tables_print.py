from controller.tools import  clear_screen
# todas las funciones imprimen los resultados en forma de tabla.
# funcion que formatea los corredores e imprime una tabla con la informacion.
def format_runner_table(runners):
    print("------------------------------------------------------------------------------------------")
    print ("{:<10} {:<12} {:<18} {:<15} {:<12} {:<4} {:<4} {:<9}".format("ID"
                                                            ,"Last Name"
                                                            ,"Second Last Name"
                                                            ,"First Name"
                                                            ,"Second Name"
                                                            ,"Sex"
                                                            ,"Age"
                                                            ,"Time"
                                                            ))
    print("------------------------------------------------------------------------------------------")
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
    print("------------------------------------------------------------------------------------------\n")

# funcion que imprime todos los corredores que participaron en una tabla.
def all_runners_table(runners):
    clear_screen()
    print("**************************************")
    print("listing all runners by table...")
    print("**************************************")
    format_runner_table(runners)
    input("*Press enter to continue*")

# funcion que imprime la cantidad de participantes por grupo etario.
def participants_age_table(runners):
    clear_screen()
    print("**************************************")
    print("listing all runners by age on table...")
    print("**************************************")
    print ("{:<10} {:<10}".format("Age group","Number of participants"))
    
    for key, value in runners.items():
        print ("{:<10} {:<12}".format(key,value))
    input("\n*Press enter to continue*")

# funcion que imprime todos los ganadores por grupos etarios.
def winners_age_table(runners):

    clear_screen()
    print("**************************************")
    print("listing all winners by age on table...")
    print("**************************************")

    if "Juniors" in runners:
        print('Juniors:')
        format_runner_table([runners['Juniors']])
    if "Seniors" in runners:
        print('Seniors:')
        format_runner_table([runners['Seniors']])
    if "Masters" in runners:
        print('Masters:')
        format_runner_table([runners['Masters']])
    input("\n*Press enter to continue*")

# funcion que imprime todos los ganadores por grupo etario y por sexo.
def winners_age_sex_table(runners):
    clear_screen()
    print("**********************************************")
    print("listing all winners by age and sex on table...")
    print("**********************************************")

    if "Juniors_Male" in runners:
        print('Juniors Male Winner:')
        format_runner_table([runners['Juniors_Male']])
    if "Juniors_Female" in runners:
        print('Juniors Female Winner:')
        format_runner_table([runners['Juniors_Female']])
    if "Seniors_Male" in runners:
        print('Seniors Male Winner:')
        format_runner_table([runners['Seniors_Male']])
    if "Seniors_Female" in runners:
        print('Seniors Female Winner:')
        format_runner_table([runners['Seniors_Female']])
    if "Masters_Male" in runners:
        print('Masters Male Winner:')
        format_runner_table([runners['Masters_Male']])
    if "Masters_Female" in runners:
        print('Masters Female Winner: ')
        format_runner_table([runners['Masters_Female']])
    input("\n*Press enter to continue*")

# funcion que imprime todos los ganadores por sexo.
def winners_sex_table(runners):

    clear_screen()
    print("**************************************")
    print("listing all winners by sex on table...")
    print("**************************************")

    if "male" in runners:
        print("Male Winner:")
        format_runner_table([runners['male']])
    if "female" in runners:
        print("Female Winner:")
        format_runner_table([runners['female']])
    input("\n*Press enter to continue*")

# funcion que imprime el promedio de tiempo por grupos etarios y por sexo.
def average_age_sex_table(runners):
    clear_screen()
    print("******************************************************")
    print("listing all averages time by age and sex on a table...")
    print("******************************************************")
    print("----------------------------------------------")
    print ("{:<15} {:<15} {:<15} ".format("Age","Sex", "Average"))
    if "juniors_male" in runners:
        print("----------------------------------------------")
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Juniors Male"
                                                                    ,"M"
                                                                    ,runners['juniors_male']))
    if "juniors_female" in runners:
        print("----------------------------------------------")
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Juniors Female"
                                                                    ,"F"
                                                                    ,runners['juniors_female']))
    if "seniors_male" in runners:
        print("----------------------------------------------")
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Seniors Male"
                                                                    ,"M"
                                                                    ,runners['seniors_male']))
    if "seniors_female" in runners:
        print("----------------------------------------------")
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Seniors Female"
                                                                    ,"F"
                                                                    ,runners['seniors_female']))
    if "masters_male" in runners:
        print("----------------------------------------------")
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Masters Male"
                                                                    ,"M"
                                                                    ,runners['masters_male']))
    if "masters_female" in runners:
        print("----------------------------------------------")
        print ("{:<15} {:<15} {:<15}".format(
                                                                    "Masters Female"
                                                                    ,"F"
                                                                    ,runners['masters_female']))
    input("\n*Press enter to continue*")