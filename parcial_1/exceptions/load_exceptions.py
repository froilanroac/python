# error para cuando haya un espacio vacio en la data del corredor
class empty_runner_field(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

# error para cuando haya un dato incorrecto en los corredores.
class incorrect_runner_field(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

# error para cuando no se cargue un archivo .txt
class incorrect_file_type(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

# error para cuando no haya data cargada en el archivo.
class empty_file(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message