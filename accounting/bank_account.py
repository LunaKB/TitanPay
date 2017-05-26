class BankAccount(object):
    def __init__(self, bank_name, account_number, routing_number):
        self.__bank_name = bank_name;
        self.__account_number = account_number;
        self.__routing_number = routing_number;
        self.__amount = 0;

    def deposit(self, amt):
        self.__amount += amt;
        print("Depositing $" + str(amt) + " in " + self.__bank_name + " Account Number: " +
              self.__account_number + " using Routing Number: " + self.__routing_number);

    def get_amount(self):
        return self.__amount;