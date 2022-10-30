from controller.tools import clear_screen
from views.tables_print import format_runner_table
# todas las funciones aqui imprimen la inforacion en una sola linea.
# imprime todos los paricipantes de la competencia.
def total_participants_line(runners):
    clear_screen()
    print("------------------------------------------------------")
    print("Total participants by line:")
    print(f"The total number of participants was {len(runners)}")
    print("------------------------------------------------------")
    input("\n*Press enter to continue*")

# fucnion que imprime los participantes por sexo.
def participants_sex_line(runners):
    clear_screen()
    print("------------------------------------------------------------------------------------------")
    print("Total participants by sex on line:")
    print(f"The total of male runners was {runners['Male']} and female runners was {runners['Female']}")
    print("------------------------------------------------------------------------------------------")
    input("\n*Press enter to continue*")

# funcion que imprime quien fue el ganador general.
def general_winner_line(runner):
    clear_screen()
    print("-----------------------")
    print("General winner by line:")
    print("-----------------------")
    if runner:
        format_runner_table([runner])
    input("\n*Press enter to continue*")

# funcion que imprime el histograma de los participantes por grupo etario.
def histogram_age_line(runners):
    clear_screen()
    print("-----------------------")
    print("Histogram by age line:")
    print("-----------------------")
    if 'juniors' in runners:
        print(f"Juniors ({round(runners['juniors'])}): | ",end="")
        for i in range(round(runners['juniors'])):
            print("*", end="")
        print()
    if 'seniors' in runners:
        print(f"Seniors ({round(runners['seniors'])}): | ",end="")
        for i in range(round(runners['seniors'])):
            print("*", end="")
        print()
    if 'masters' in runners:
        print(f"Masters ({round(runners['masters'])}): | ",end="")
        for i in range(round(runners['masters'])):
            print("*", end="")
        print()
    input("\n*Press enter to continue*")
