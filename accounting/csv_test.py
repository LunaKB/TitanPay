from employee import HourlyEmployee, SalariedEmployee;
from payment_method import MailPayment, PickUpPayment, DirectDepositPayment;
import csv;
import datetime;
from locale import *;

setlocale(LC_NUMERIC, '');
employees = [];

with open('../data/hourly_employees.csv', newline='') as csvfile:
    hourly_employee_data = csv.DictReader(csvfile);

    for row in hourly_employee_data:
        id = row['EmployeeId'];
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

        employees.append(HourlyEmployee(id, first_name, last_name, union_dues, hourly_rate, payment_method));

with open('../data/salaried_employees.csv', newline='') as csvfile:
    salaried_employee_data = csv.DictReader(csvfile);

    for row in salaried_employee_data:
        id = row['EmployeeId'];
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

        employees.append(SalariedEmployee(id, first_name, last_name, union_dues, salary, comm_rate, payment_method));


with open('../data/timecards.csv', newline='') as csvfile:
    time_card_data = csv.DictReader(csvfile);

    for row in time_card_data:
        id = row['EmployeeId'];
        in_time = datetime.datetime.strptime(row['Date'] + " " + row['In'],"%m/%d/%Y %H%M");
        out_time = datetime.datetime.strptime(row['Date'] + " " + row['Out'],"%m/%d/%Y %H%M");
        for emp_row in employees:
            if emp_row.get_id() == id:
                emp_row.clock_in(in_time);
                emp_row.clock_out(out_time);

with open('../data/receipts.csv', newline='') as csvfile:
    receipt_data = csv.DictReader(csvfile);

    for row in receipt_data:
        id = row['EmployeeId'];
        total = atof(row["Total"]);
        for emp_row in employees:
            if emp_row.get_id() == id:
                emp_row.make_sale(total);


start_date = datetime.datetime.strptime("6/20/2016","%m/%d/%Y").date();
end_date = datetime.datetime.strptime("6/29/2016","%m/%d/%Y").date();

for emp in employees:
    print(emp.get_full_name() + "\t||\t" + emp.calculate_pay(start_date, end_date));