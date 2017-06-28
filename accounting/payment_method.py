from address import Address
from bank_account import BankAccount

class PaymentMethod:
    def __init__(self, payment_method):
        self.__payment_method = payment_method;


class MailPayment(PaymentMethod):
    def __init__(self, address, city, state, zip_code):
        PaymentMethod.__init__(self, 'mail');
        self.__address = Address(address, city, state, zip_code);

    def pay(self, name, total):
        return("Mailing a check to %s for %s to %s" % (name, '${:,.2f}'.format(total), self.__address.get_address()));


class PickUpPayment(PaymentMethod):
    def __init__(self):
        PaymentMethod.__init__(self, 'pick up');

    def pay(self, name, total):
        return ("A check for %s is waiting for %s at the PostMaster." %('${:,.2f}'.format(total), name));


class DirectDepositPayment(PaymentMethod):
    def __init__(self, bank_name, routing_number, account_id):
        PaymentMethod.__init__(self, 'direct deposit');
        self.__bank_account = BankAccount(bank_name, routing_number, account_id);

    def pay(self, name, total):
        return self.__bank_account.deposit(total);
