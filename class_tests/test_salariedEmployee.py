from unittest import TestCase
from accounting.employee import SalariedEmployee;
from accounting.payment_method import PickUpPayment


class TestSalariedEmployee(TestCase):
    def test_new_employee_has_no_receipts(self):
        #arrange
        emp = SalariedEmployee(3, "name", "name", 30, 15000, 0.1, PickUpPayment());

        #assert
        count = emp.get_receipt_count();
        self.assertEqual(count, 0);

    def test_make_sale(self):
        #arrange
        emp = SalariedEmployee(3, "name", "name", 30, 15000, 0.1, PickUpPayment());

        #act
        emp.make_sale(100);

        # assert
        count = emp.get_receipt_count();
        self.assertEqual(count, 1);

    def test_calculate_pay(self):
        #arrange
        emp = SalariedEmployee(3, "name", "name", 30, 15000, 0.1, PickUpPayment());

        #act
        for i in range(1,6):
            amount = 100 * i;
            emp.make_sale(amount);

        #assert
        emp.calculate_pay("", "");
        pay = emp.get_last_pay_amount();
        self.assertGreater(pay, 0);