from unittest import TestCase;
from accounting.employee import HourlyEmployee;
from accounting.payment_method import PickUpPayment;
import datetime;


class TestHourlyEmployee(TestCase):
    def test_new_employee_has_no_time_cards(self):
        #arrange
        emp = HourlyEmployee(3, "name", "name", 30, 15, PickUpPayment());

        #assert
        count = emp.get_time_card_count();
        self.assertEqual(count, 0);

    def test_clock_in(self):
        #arrange 
        emp = HourlyEmployee(3, "name", "name", 30, 15, PickUpPayment());

        #act
        emp.clock_in(datetime.datetime.strptime("6/20/2016 1700","%m/%d/%Y %H%M"));

        #assert
        count = emp.get_time_card_count();
        self.assertEqual(count, 1)


    def test_clock_out(self):
        #arrange
        emp = HourlyEmployee(3, "name", "name", 30, 15, PickUpPayment());

        #act
        emp.clock_in(datetime.datetime.strptime("6/20/2016 900","%m/%d/%Y %H%M"));
        result = emp.clock_out(datetime.datetime.strptime("6/20/2016 1700","%m/%d/%Y %H%M"))

        #assert
        self.assertTrue(result);

    def test_calculate_pay(self):
        #arrange
        emp = HourlyEmployee(3, "name", "name", 30, 15, PickUpPayment());
        start_date = datetime.datetime.strptime("6/1/2016", "%m/%d/%Y").date();
        end_date = datetime.datetime.strptime("6/6/2016", "%m/%d/%Y").date();
        in_time = "900";
        out_time = "1700";

        #act
        for i in range(1, 6):
            date = "6/%d/2016" %(i);
            in_time_str = "%s %s" % (date, in_time);
            out_time_str = "%s %s" %(date, out_time);

            emp.clock_in(datetime.datetime.strptime(in_time_str, "%m/%d/%Y %H%M"));
            emp.clock_out(datetime.datetime.strptime(out_time_str, "%m/%d/%Y %H%M"))

        #assert
        emp.calculate_pay(start_date, end_date);
        pay = emp.get_last_pay_amount();
        self.assertGreater(pay, 0);
