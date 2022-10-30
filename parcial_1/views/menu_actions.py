from controller.tools import clear_screen, exit
from controller.logic import participants_by_age, participants_by_sex, winners_by_age, winners_by_sex_age, winners_by_sex,general_winner, histogram_data, average_age_sex
from views.tables_print import all_runners_table, participants_age_table, winners_age_table, winners_age_sex_table, winners_sex_table, average_age_sex_table
from views.line_print import total_participants_line, participants_sex_line, general_winner_line, histogram_age_line
import controller.config as config

# menu de acciones de la aplicacion.
def menu_actions():
    clear_screen()

    menu_options = {
    "1": "List of all participants         (table)",
    "2": "Total participants               (line)",
    "3": "Total Participants by age        (table)",
    "4": "Number of participants by sex    (line)",
    "5": "Winners by age                   (table)",
    "6": "Winners by sex                   (table)",
    "7": "Winners by age and sex           (table)",
    "8": "General winner                   (line)",
    "9": "Histogram of participants by age (histogram)",
    "10": "Average time by age and sex     (table)",
    "11": "Go to main menu\n"}

    while True:
        clear_screen()
        print("*********************Menu Actions*********************")
        print("------------------------------------------------------")
        print("Options:\n")
        for key, value in menu_options.items():
            print(key, value)

        option = input('Please, Select an option:\n')
            
        if option == "1":
            clear_screen()
            all_runners_table(config.runners)
        elif option == "2":
            clear_screen()
            total_participants_line(config.runners)
        elif option == "3":
            clear_screen()
            participants_age_table(participants_by_age())
        elif option == "4":
            clear_screen()
            participants_sex_line(participants_by_sex())
        elif option == "5":
            clear_screen()
            winners_age_table(winners_by_age())
        elif option == "6":
            clear_screen()
            winners_sex_table(winners_by_sex())
        elif option == "7":
            clear_screen()
            winners_age_sex_table(winners_by_sex_age())
        elif option == "8":
            clear_screen()
            general_winner_line(general_winner())
        elif option == "9":
            clear_screen()
            histogram_age_line(histogram_data())
        elif option == "10":
            clear_screen()
            average_age_sex_table(average_age_sex())
        elif option == "11":
            break
        else:
            print('Invalid option, please try again.')
            input("\n*Press enter to continue*")