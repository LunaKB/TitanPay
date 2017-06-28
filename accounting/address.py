class Address:

    def __init__(self, address, city, state, zip_code):
        self.__street_address = address
        self.__city = city
        self.__state = state
        self.__zip = zip_code

    def get_address(self):
        full_address = self.__street_address + ' ' + self.__city + ', ' + self.__state + '. ' + self.__zip
        return full_address