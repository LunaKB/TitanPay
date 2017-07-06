from unittest import TestCase
from accounting.employee import HourlyEmployee
from datetime import datetime


class TestHourlyEmployee(TestCase):
    def test_clock_in(self):
        test_employee = HourlyEmployee('', '', '', '', '', '')
        test_employee.clock_in(datetime.now())
        self.assertEquals(datetime.now(), test_employee.clock_in(datetime.now()))

    def test_clock_out(self):
        test_employee = HourlyEmployee('', '', '', '', '', '')
        test_employee.clock_out(datetime.now())
        self.assertEquals(datetime.now(), test_employee.clock_out(datetime.now()))

    def test_calculate_pay(self):
        test_employee = HourlyEmployee('', '', '', '', '', '')
        test_employee.calculate_pay(datetime.now().date(),datetime.now().date())
        self.assertEquals(0, test_employee.calculate_pay(datetime.now().date(),datetime.now().date()))
