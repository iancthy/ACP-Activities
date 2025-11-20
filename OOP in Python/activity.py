class Contact:
    def __init__(self, name, number):
        self.__name = name     
        self.__number = number  

    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def set_number(self, new_number):
        self.__number = new_number

alice = Contact("Alice", "09123456789")

print("Name:", alice.get_name())
print("Number:", alice.get_number())

alice.set_number("09987654321")
print("Updated Number:", alice.get_number())
