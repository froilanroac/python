from controller.tools import exit, clear_screen
from views.menu_file import menu_file
from views.menu_actions import menu_actions

def menu():

    menu_options = {"1": "File", "2": "Actions", "3": "Finish Program"}

    while True:
        clear_screen()

        for key, value in menu_options.items():
            print(key, value)

        option = input('Please, Select an option:\n')
        
        if option == "1":
            menu_file()
        elif option == "2":
            menu_actions()
        elif option == "3":
            exit()
        else:
            print('Invalid Option, please try again.')
            

        

