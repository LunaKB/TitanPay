from unittest import TestCase
from accounting.employee import SalariedEmployee
from datetime import datetime


class TestSalariedEmployee(TestCase):
    def test_make_sale(self):
        test_employee = SalariedEmployee('', '', '', '', '', '', '')
        test_employee.make_sale(1)
        self.assertEquals(1, test_employee.get_receipt_count())

    def test_calculate_pay(self):
        test_employee = SalariedEmployee('', '', '', '', '', '','')
        test_employee.calculate_pay(datetime.now().date(), datetime.now().date())
        self.assertEquals(0, test_employee.calculate_pay(datetime.now().date(), datetime.now().date()))
