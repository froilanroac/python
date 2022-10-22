from controller.tools import clear_screen, exit
from controller.logic import load_runners, participants_by_age, participants_by_sex, winners_by_age, winners_by_sex_age, winners_by_sex,general_winner, histogram_data, average_age_sex
from views.tables_print import all_runners_table, participants_age_table, winners_age_table, winners_age_sex_table, winners_sex_table, average_age_sex_table
from views.line_print import total_participants_line, participants_sex_line, general_winner_line, histogram_age_line
import controller.config as config
def menu_actions():
    load_runners()
    clear_screen()

    menu_options = {"1": "List of all participants by table","2":"Total amount of participants by line","3": "Participants by age by table","11": "Go to main menu"}

    while True:
        for key, value in menu_options.items():
            print(key, value)

        option = input('Please, Select an option:\n')
            
        if option == "1":
            all_runners_table(config.runners)
        if option == "2":
            total_participants_line(config.runners)
        if option == "3":
            participants_age_table(participants_by_age())
        if option == "4":
            participants_sex_line(participants_by_sex())
        if option == "5":
            winners_age_table(winners_by_age())
        if option == "6":
            winners_sex_table(winners_by_sex())
        if option == "7":
            winners_age_sex_table(winners_by_sex_age())
        if option == "8":
            general_winner_line(general_winner())
        if option == "9":
            histogram_age_line(histogram_data())
        if option == "10":
            average_age_sex_table(average_age_sex())
        
        elif option == "11":
            break
        else:
            print('Invalid Option, please try again.')