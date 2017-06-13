import address
import bank_account

class PaymentMethod:
    def __init__(self, payment_method):
        self.__payment_method = payment_method


class MailPayment(PaymentMethod):
    def __init__(self):
        PaymentMethod.__init__(self, 'mail')
        self.__address = Address(address, city, state, zip_code)

    def pay(self, name, total):
        return "%s %s %s %s %s %s" \
               % ('Mailing a check to', name,
                  'for', total, 'to', self.__address.get_address())


class PickUpPayment(PaymentMethod):
    def __init__(self):
        PaymentMethod.__init__(self, 'pick up')

    def pay(self, name, total):
        return "%s %s %s %s %s" \
               % ('A check for', total, 'is waiting for', name,
                  'at the PostMaster.')


class DirectDepositPayment(PaymentMethod):
    def __init__(self):
        PaymentMethod.__init__(self, 'direct deposit')
        self.__bank_account = BankAccount(bank_name, routing_number, account_id)

    def pay(self, name, total):
        return self.__bank_account.deposit(total)
