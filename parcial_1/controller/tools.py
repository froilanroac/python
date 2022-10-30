import os 
import sys

# funcion para limpiar pantalla.
def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

# funcion para salir del programa.
def exit():
    sys.exit()