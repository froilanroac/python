import os 
import sys

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def exit():
    sys.exit()