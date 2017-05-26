class SalariedEmployee(object):
    def __init__(self, firstName, lastName):
        self.__first_name = firstName;
        self.__last_name = lastName;

    def get_full_name(self):
        full_name = self.__last_name + ", " + self.__first_name;
        return full_name;


