import os 
import sys
from views.file import menu_file

def menu():

    menu_options = {"1": "File", "2": "Actions", "3": "Finish Program"}
    runners = []

    while True:
        print()
        print()
        for key, value in menu_options.items():
            print(key, value)
        option = input('Please, Select an option:\n')
        # os.system('cls' if os.name=='nt' else 'clear')

        if option not in menu_options.keys():
            print('Invalid Option, please try again.')

        elif option == "1":
            menu_file()
        elif option == "2":
            print('Actions')
        elif option == "3":
            sys.exit()

        

