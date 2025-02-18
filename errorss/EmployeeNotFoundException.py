class EmployeeNotFoundException(Exception):
    def __init__(self, message="..... Employee Not found ....."):
        self.__message = message
        super().__init__(self.__message)
