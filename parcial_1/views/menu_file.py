from controller.logic import load_runners
from controller.tools import clear_screen, exit
def menu_file():

    menu_options = {"1": "Load File", "2": "Go to main menu", "3": "Finish program"}

    while True:
        for key, value in menu_options.items():
            print(key, value)

        option = input('Please, Select an option:\n')
            
        if option == "1":
            try:
                load_runners()
                print('File loaded successfully...')
            except Exception as e:
                print(f"An error has ocurred: {e} Try again.")
        elif option == "2":
            break
        elif option == "3":
            exit()

        else:
            print('Invalid Option, please try again.')