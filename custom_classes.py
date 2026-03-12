class Calculator:
    def __init__(self):
        self.__current_val = 0

    def multiply(self, x, y):
        self.__current_val = x * y
        return self.__current_val