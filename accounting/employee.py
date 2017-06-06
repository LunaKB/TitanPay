class Employee:
    def __init__(self, employee_id, first_name, last_name, weekly_dues):
        self.__employee_id = employee_id;
        self.__first_name = first_name;
        self.__last_name = last_name;
        self.__weekly_dues = weekly_dues;

    def get_full_name(self):
        return "%s, %s" % (self.__last_name, self.__first_name)
    
    
class HourlyEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, weekly_dues, hourly_rate):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues)
        self.__hourly_rate = hourly_rate


class SalariedEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, weekly_dues, salary, commission_rate):
        Employee.__init__(self, employee_id, first_name, last_name, salary, commission_rate)
        self.__salary = salary
        self.__commission_rate = commission_rate
