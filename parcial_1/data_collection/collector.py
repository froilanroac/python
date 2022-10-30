from exceptions.load_exceptions import incorrect_file_type
from controller.data_logic import validate_file,arrange_data

# funcion que aplica la validacion a cada linea y regresa la data arreglada como una lista de diccionarios por cada corredor.
def get_data(file_name = 'competencia.txt'):
    if ".txt" in file_name:
        file = open(f"parcial_1/{file_name}", "rt")
        validate_file(file)
        file.seek(0)
        data = arrange_data(file)
        file.close()
        return data        
    else:
        raise incorrect_file_type("The file type is not .txt")

