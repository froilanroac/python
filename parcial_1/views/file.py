import os 
import sys
import controller.config as config
from controller.logic import load_runners
def menu_file():
    file_options = {"1": "Load File", "2": "Go to main menu", "3": "Finish program"}

    while True:
        print()
        print()
        for key, value in file_options.items():
            print(key, value)
        option = input('Please, Select an option:\n')

        if option not in file_options.keys():
            print('Invalid Option, please try again.')

        elif option == "1":
            try:
                load_runners()
                print('File loaded successfully...')
            except Exception as e:
                print(f"An error has ocurred: {e} Try again.")
        elif option == "2":
            break
        elif option == "3":
            print(config.runners)