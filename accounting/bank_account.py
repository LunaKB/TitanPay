class BankAccount:
    def __init__(self, bank_name, routing_number, account_id):
        self.__bank_name = bank_name;
        self.__routing_number = routing_number;
        self.__account_id = account_id;

    def deposit(self, amt):
        return ("Depositing %s in %s Account Number: %d using Routing Number: %d" %
              ('${:,.2f}'.format(amt), self.__bank_name, self.__account_id, self.__routing_number));