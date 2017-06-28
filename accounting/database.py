import sqlite3

class Database:
    def __init__(self):
        self.__file = '../data/TitanPay.sqlite';
        self.__connection = lambda: None;
        self.__cursor = lambda: None;


        self.__table_hourly_employees = "hourly_employees";
        self.__column_rate = "hourly_rate";

        self.__table_salaried_employees = "salaried_employees";
        self.__column_commission = "commission_rate";
        self.__column_salary = "salary";

        self.__column_emp_id = "employee_id";
        self.__column_last_name = "last_name";
        self.__column_first_name = "first_name";
        self.__column_union_dues = "union_dues";
        self.__column_payment_method = "payment_method";

        self.__table_receipts = "receipts";
        self.__column_item = "item";
        self.__column_units = "units";
        self.__column_unit_cost = "unit_cost";
        self.__column_total = "total";

        self.__table_time_cards = "time_cards";
        self.__column_in = "in_time";
        self.__column_out = "out_time";
        self.__column_date = "date";

        self.__column_id = "id";
        self.__field_int = "INTEGER";
        self.__field_text = "TEXT";
        self.__field_float = "REAL";

        self.__create_tables();

    def __connect(self):
        self.__connection = sqlite3.connect(self.__file);
        self.__cursor = self.__connection.cursor();

    def __commit(self):
        self.__connection.commit();

    def __disconnect(self):
        self.__connection.close();

    def __create_hourly_table(self):
        hourly_table = False;
        try:
            self.__cursor.execute(
                'CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_hourly_employees,
                                                                   nf=self.__column_emp_id,
                                                                   ft=self.__field_int));
        except:
            hourly_table = True;
            
        if hourly_table == False:
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_last_name,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_first_name,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_rate,
                                                                 ct=self.__field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_union_dues,
                                                                 ct=self.__field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_payment_method,
                                                                 ct=self.__field_text));

    def __create_salary_table(self):
        salary_table = False;
        try:
            self.__cursor.execute(
                'CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_salaried_employees,
                                                                                 nf=self.__column_emp_id,
                                                                                 ft=self.__field_int));
        except:
            salary_table = True;

        if salary_table == False:
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_last_name,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_first_name,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_salary,
                                                                 ct=self.__field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_commission,
                                                                 ct=self.__field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_union_dues,
                                                                 ct=self.__field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_payment_method,
                                                                 ct=self.__field_text));

    def __create_receipt_table(self):
        receipt_table = False;
        try:
            self.__cursor.execute(
                'CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_receipts,
                                                                                 nf=self.__column_id,
                                                                                 ft=self.__field_int));
        except:
            receipt_table = True;
            
        if receipt_table == False:
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                 cn=self.__column_emp_id,
                                                                 ct=self.__field_int));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                 cn=self.__column_first_name,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                 cn=self.__column_item,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                 cn=self.__column_units,
                                                                 ct=self.__field_int));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                 cn=self.__column_unit_cost,
                                                                 ct=self.__field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                 cn=self.__column_total,
                                                                 ct=self.__field_float));

    def __create_card_table(self):
        card_table = False;
        try:
            self.__cursor.execute(
                'CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_time_cards,
                                                                                 nf=self.__column_id,
                                                                                 ft=self.__field_int));
        except:
            card_table = True;
            
        if  card_table == False:
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                 cn=self.__column_emp_id,
                                                                 ct=self.__field_int));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                 cn=self.__column_in,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                 cn=self.__column_out,
                                                                 ct=self.__field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                 cn=self.__column_date,
                                                                 ct=self.__field_text));
    def __create_tables(self):
        self.__connect();
        
        self.__create_hourly_table();
        self.__create_salary_table();
        self.__create_receipt_table();
        self.__create_card_table();
        
        self.__commit();
        self.__disconnect();


    def insert_hourly_employee(self, id, last_name, first_name, rate, union_dues, payment_method):
        self.__connect();
        param = [];
        param.extend((id, last_name, first_name, rate, union_dues, payment_method));

        try:
            self.__cursor.execute(
                "INSERT INTO {tn} ({id}, {lname}, {fname}, {rate}, {union}, {method}) VALUES(?, ?, ?, ?, ?, ?)"
                    .format(tn=self.__table_hourly_employees,
                            id=self.__column_emp_id,
                            lname=self.__column_last_name,
                            fname= self.__column_first_name,
                            rate=self.__column_rate,
                            union=self.__column_union_dues,
                            method=self.__column_payment_method), param);
        except sqlite3.IntegrityError:
            print("Employee %d already inserted" %(id));

        self.__commit();
        self.__disconnect();

    def get_all_hourly_employees(self):
        self.__connect();

        self.__cursor.execute("SELECT * FROM {tn}".format(tn=self.__table_hourly_employees));
        rows = self.__cursor.fetchall();

        self.__commit();
        self.__disconnect();

        return rows;

    def insert_salary_employee(self, id, last_name, first_name, salary, commission, union_dues, payment_method):
        self.__connect();
        param = [];
        param.extend((id, last_name, first_name, salary, commission, union_dues, payment_method));

        try:
            self.__cursor.execute(
                "INSERT INTO {tn} ({id}, {lname}, {fname}, {salary}, {comm}, {union}, {method}) VALUES(?, ?, ?, ?, ?, ?, ?)"
                    .format(tn=self.__table_salaried_employees,
                            id=self.__column_emp_id,
                            lname=self.__column_last_name,
                            fname= self.__column_first_name,
                            salary=self.__column_salary,
                            comm=self.__column_commission,
                            union=self.__column_union_dues,
                            method=self.__column_payment_method), param);
        except sqlite3.IntegrityError:
            print("Employee %d already inserted" %(id));

        self.__commit();
        self.__disconnect();

    def insert_receipt(self, id, first_name,  item, units, cost, total):
        self.__connect();
        param = [];
        param.extend((id, first_name, item, units, cost, total));

        self.__cursor.execute(
            "INSERT INTO {tn} ({id}, {fname}, {item}, {units}, {cost}, {total}) VALUES(?, ?, ?, ?, ?, ?)"
                .format(tn=self.__table_receipts,
                        id=self.__column_emp_id,
                        fname=self.__column_first_name,
                        item=self.__column_item,
                        units=self.__column_units,
                        cost=self.__column_unit_cost,
                        total=self.__column_total), param);

        self.__commit();
        self.__disconnect();

    def insert_time_card(self, id,in_time, out_time, date):
        self.__connect();
        param = [];
        param.extend((id,in_time, out_time, date));

        self.__cursor.execute(
            "INSERT INTO {tn} ({id}, {in_t}, {out_t}, {date}) VALUES(?, ?, ?, ?)"
                .format(tn=self.__table_time_cards,
                        id=self.__column_emp_id,
                        in_t=self.__column_in,
                        out_t=self.__column_out,
                        date=self.__column_date), param);

        self.__commit();
        self.__disconnect();
