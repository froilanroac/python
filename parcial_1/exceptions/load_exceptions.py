class empty_runner_field(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

class incorrect_runner_field(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

class incorrect_file_type(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message

class empty_file(Exception):
    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return self.message