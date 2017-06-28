class Receipt:
    def __init__(self, sale_amount):
        self.__sale_amount = sale_amount;

    def get_sale_amount(self):
        return self.__sale_amount;