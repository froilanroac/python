from controller.tools import exit, clear_screen
from controller.logic import data
from views.menu_file import menu_file
from views.menu_actions import menu_actions

def main_menu():

    menu_options = {"1": " File", "2": " Actions", "3": " Finish Program"}

    while True:

        clear_screen()
        print("*********************Parcial 1*********************")
        print("---------------------------------------------------")
        print("Options:\n")

        for key, value in menu_options.items():
            print(key, value)

        option = input('Please, Select an option:\n')
        
        if option == "1":
            menu_file()
        elif option == "2":
            if data():
                menu_actions()
            else:
                input("Error, there is not data loaded, please load a file first.")
        elif option == "3":
            exit()
        else:
            print('Invalid option, please try again.')
            input("\n*Press enter to continue*")
            

        

