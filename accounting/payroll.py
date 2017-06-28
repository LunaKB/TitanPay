from employee import HourlyEmployee, SalariedEmployee;
from payment_method import MailPayment, PickUpPayment, DirectDepositPayment;
from database import Database;
import csv;
import datetime;
from locale import *;

class Payroll:
    def __init__(self):
        setlocale(LC_NUMERIC, '');
        self.__database = Database();
        self.__employees = [];

    def __read_hourly_employees(self):
        with open('../data/hourly_employees.csv', newline='') as csvfile:
            hourly_employee_data = csv.DictReader(csvfile);

            for row in hourly_employee_data:
                id = int(row['EmployeeId']);
                last_name = row['LastName'];
                first_name = row['FirstName'];
                hourly_rate = float(row['HourlyRate']);
                abbr_pay_method = row['PaymentMethod'];
                payment_method = lambda: None;

                try:
                    union_dues = float(row['UnionDues']);
                except ValueError:
                    union_dues = 0.0;


                if abbr_pay_method == " DD ":
                    payment_method = DirectDepositPayment("Generic", 0, 0);
                elif abbr_pay_method == " PU ":
                    payment_method = PickUpPayment();
                elif abbr_pay_method == " MA ":
                    payment_method = MailPayment("Generic", "Generic", "Generic", "Generic");

                self.__database.insert_hourly_employee(id, last_name, first_name, hourly_rate, union_dues, abbr_pay_method);


    def __read_salaried_employees(self):
        with open('../data/salaried_employees.csv', newline='') as csvfile:
            salaried_employee_data = csv.DictReader(csvfile);

            for row in salaried_employee_data:
                id = int(row['EmployeeId']);
                last_name = row['LastName'];
                first_name = row['FirstName'];
                salary = float(row['Salary']);
                comm_rate =  float(row['CommissionRate'])/100;
                abbr_pay_method = row['PaymentMethod'];
                payment_method = lambda: None;

                try:
                    union_dues = float(row['UnionDues']);
                except ValueError:
                    union_dues = 0.0;


                if abbr_pay_method == " DD ":
                    payment_method = DirectDepositPayment("Generic", 0, 0);
                elif abbr_pay_method == " PU ":
                    payment_method = PickUpPayment();
                elif abbr_pay_method == " MA ":
                    payment_method = MailPayment("Generic", "Generic", "Generic", "Generic");

                self.__employees.append(SalariedEmployee(id, first_name, last_name, union_dues, salary, comm_rate, payment_method));
                self.__database.insert_salary_employee(id, last_name, first_name, salary, comm_rate, union_dues, abbr_pay_method);



    def __read_time_cards(self):
        with open('../data/timecards.csv', newline='') as csvfile:
            time_card_data = csv.DictReader(csvfile);

            for row in time_card_data:
                id = row['EmployeeId'];
                in_time = row['In']; #datetime.datetime.strptime(row['Date'] + " " + row['In'],"%m/%d/%Y %H%M");
                out_time = row['Out']; #datetime.datetime.strptime(row['Date'] + " " + row['Out'],"%m/%d/%Y %H%M");
                date = row['Date'];
                self.__database.insert_time_card(id, in_time, out_time, date);
                # for emp_row in self.__employees:
                #     if emp_row.get_id() == id:
                #         emp_row.clock_in(in_time);
                #         emp_row.clock_out(out_time);

    def __read_receipts(self):
        with open('../data/receipts.csv', newline='') as csvfile:
            receipt_data = csv.DictReader(csvfile);

            for row in receipt_data:
                id = row['EmployeeId'];
                first_name = row['FirstName'];
                item = row['Item'];
                units = int(row['Units']);
                cost = float(row['Unit Cost']);
                total = atof(row['Total']);

                self.__database.insert_receipt(id, first_name, item, units, cost, total);
                # for emp_row in self.__employees:
                #     if emp_row.get_id() == id:
                #         emp_row.make_sale(total);

    def __process_hourly_employees(self):
        employees = self.__database.get_all_hourly_employees();

        for row in employees:
            id = row[0];
            last_name = row[1];
            first_name = row[2];
            rate = float(row[3]);
            union_dues = float(row[4]);
            abbr_pay_method = row[5];
            payment_method = lambda: None;

            if abbr_pay_method == " DD ":
                payment_method = DirectDepositPayment("Generic", 0, 0);
            elif abbr_pay_method == " PU ":
                payment_method = PickUpPayment();
            elif abbr_pay_method == " MA ":
                payment_method = MailPayment("Generic", "Generic", "Generic", "Generic");

            self.__employees.append(HourlyEmployee(id, first_name, last_name, union_dues, rate, payment_method));


    def process_payroll(self, label):
        self.__read_hourly_employees();
        self.__read_salaried_employees();
        self.__read_time_cards();
        self.__read_receipts();
        self.__process_hourly_employees();

        # message = '';
        # start_date = datetime.datetime.strptime("6/20/2016","%m/%d/%Y").date();
        # end_date = datetime.datetime.strptime("6/29/2016","%m/%d/%Y").date();
        #
        # for emp in self.__employees:
        #     message += emp.get_full_name() + " " + emp.calculate_pay(start_date, end_date) + '\n';
        #label.config(text=message);

pay = Payroll();
pay.process_payroll(4);
