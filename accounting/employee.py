# The pay method in the PaymentMethod subclasses are assumed to take a
# name and number, in that order.
# Ex: def pay(self, name, amt)

from datetime import date, timedelta, datetime;
from receipt import Receipt;
from time_card import TimeCard;

class Employee:
    def __init__(self, employee_id, first_name, last_name, weekly_dues, payment_method):
        self.__employee_id = employee_id;
        self.__first_name = first_name;
        self.__last_name = last_name;
        self.__weekly_dues = weekly_dues;
        self.__payment_method = payment_method;

    def get_id(self):
        return self.__employee_id;

    def get_first_name(self):
        return self.__first_name;

    def get_last_name(self):
        return self.__last_name;

    def get_full_name(self):
        return "%s, %s" % (self.__last_name, self.__first_name)

    def get_union_dues(self):
        return self.__weekly_dues;

    def get_payment_method(self):
        return self.__payment_method;


class HourlyEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, weekly_dues, hourly_rate, payment_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, payment_method);
        self.__hourly_rate = hourly_rate;
        self.__time_cards = [];

    def clock_in(self, in_date):
        #current_dt = datetime.now();
        self.__time_cards.append(TimeCard(in_date.date(), in_date.time()));

    def clock_out(self, out_date):
        for time_card in self.__time_cards:
            if time_card.get_date() == out_date.date(): #datetime.now().date():
                #This will result in a total pay of $0.00 in payment calculation.
                tmp_time = datetime.now();

                # Uncomment following line to see the result if the HourlyEmployee worked 9 hours per TimeCard
                #tmp_time = datetime.now()+ timedelta(hours=9);
                time_card.set_end_time(out_date.time());

    # The calculate_pay method requires datetime.now().date() for the
    # parameters start_date and end_date.
    def calculate_pay(self, start_date, end_date):
        total = 0;
        for time_card in self.__time_cards:
            if time_card.get_date() >= start_date and time_card.get_date() <= end_date:
                total += time_card.calculate_daily_pay(self.__hourly_rate);
        total -= self.get_union_dues();
        if total <= 0:
            total = 0;
        return self.get_payment_method().pay("%s %s" % (self.get_first_name(), self.get_last_name()), total);


class SalariedEmployee(Employee):
    def __init__(self, employee_id, first_name, last_name, weekly_dues, salary, commission_rate, payment_method):
        Employee.__init__(self, employee_id, first_name, last_name, weekly_dues, payment_method);
        self.__salary = salary;
        self.__commission_rate = commission_rate;
        self.__receipts = [];

    def make_sale(self, amt):
        #current_dt = datetime.now();
        self.__receipts.append(Receipt(amt)); #current_dt.date(), amt));

    # The calculate_pay method requires datetime.now().date() for the
    # parameters start_date and end_date.
    def calculate_pay(self, start_date, end_date):
        total = 0;
        for receipt in self.__receipts:
            #if receipt.get_date() <= start_date and receipt.get_date() >= end_date:
            total += (self.__commission_rate * receipt.get_sale_amount());
        total -= self.get_union_dues();
        if total <= 0:
            total = 0;
        return self.get_payment_method().pay("%s %s" % (self.get_first_name(), self.get_last_name()), total);
