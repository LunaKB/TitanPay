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
        self.__column_in = "in";
        self.__column_out = "out";
        self.__column_date = "date";

        self.__column_id = "id";


        #self.__table_employees = "employees";
        #self.__column_type = "type";

        # self.__table_mail = "mail";
        # self.__column_street_address = "street_address";
        # self.__column_city = "city";
        # self.__column_state = "state";
        # self.__column_zip_code = "zip_code";
        #
        # self.__table_direct_deposit = "direct_deposit";
        # self.__column_id = "employee_id";
        # self.__column_account_number = "account_number";
        # self.__column_routing_number = "routing_number";
        #
        # self.__table_pick_up = "pick_up";
        # self.__column_post_master = "post_master";

        self.__create_tables();

    def __connect(self):
        self.__connection = sqlite3.connect(self.__file);
        self.__cursor = self.__connection.cursor();

    def __commit(self):
        self.__connection.commit();

    def __disconnect(self):
        self.__connection.close();

    def __create_tables(self):
        self.__connect();

        field_int = "INTEGER";
        field_text = "TEXT";
        field_float = "REAL";
        hourly_table = False;
        salary_table = False;
        receipt_table = False;
        card_table = False;

        # try:
        #     self.__cursor.execute(
        #         'CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_employees,
        #                                                                          nf=self.__column_id,
        #                                                                          ft=field_int));
        #     self.__cursor.execute(
        #         "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_employees,
        #                                                          cn=self.__column_first_name,
        #                                                          ct=field_text));
        #     self.__cursor.execute(
        #         "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_employees,
        #                                                          cn=self.__column_last_name,
        #                                                          ct=field_text));
        #     self.__cursor.execute(
        #         "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_employees,
        #                                                          cn=self.__column_type,
        #                                                          ct=field_text));
        #     self.__cursor.execute(
        #         "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_employees,
        #                                                          cn=self.__column_union_dues,
        #                                                          ct=field_float));
        #     self.__cursor.execute(
        #         "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_employees,
        #                                                          cn=self.__column_payment_method,
        #                                                          ct=field_text));
        try:
            self.__cursor.execute(
                'CREATE TABLE {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_hourly_employees,
                                                                   nf=self.__column_emp_id,
                                                                   ft=field_int));
        except:
            hourly_table = True;

        if hourly_table == False:
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_last_name,
                                                                 ct=field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_first_name,
                                                                 ct=field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_rate,
                                                                 ct=field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_union_dues,
                                                                 ct=field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_hourly_employees,
                                                                 cn=self.__column_payment_method,
                                                                 ct=field_text));

        try:
            self.__cursor.execute(
                'CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_salaried_employees,
                                                                                 nf=self.__column_emp_id,
                                                                                 ft=field_int));
        except:
            salary_table = True;

        if salary_table == False:
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_last_name,
                                                                 ct=field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_first_name,
                                                                 ct=field_text));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_salary,
                                                                 ct=field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_commission,
                                                                 ct=field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_union_dues,
                                                                 ct=field_float));
            self.__cursor.execute(
                "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_salaried_employees,
                                                                 cn=self.__column_payment_method,
                                                                 ct=field_text));

            try:
                self.__cursor.execute(
                    'CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_receipts,
                                                                                     nf=self.__column_id,
                                                                                     ft=field_int));
            except:
                receipt_table = True;

            if receipt_table == False:
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                     cn=self.__column_emp_id,
                                                                     ct=field_int));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                     cn=self.__column_first_name,
                                                                     ct=field_text));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                     cn=self.__column_item,
                                                                     ct=field_text));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                     cn=self.__column_units,
                                                                     ct=field_int));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                     cn=self.__column_unit_cost,
                                                                     ct=field_float));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_receipts,
                                                                     cn=self.__column_total,
                                                                     ct=field_float));

            try:
                self.__cursor.execute(
                    'CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_time_cards,
                                                                                     nf=self.__column_id,
                                                                                     ft=field_int));
            except:
                card_table = True;

            if  card_table == False:
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                     cn=self.__column_emp_id,
                                                                     ct=field_int));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                     cn=self.__column_in,
                                                                     ct=field_text));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                     cn=self.__column_out,
                                                                     ct=field_text));
                self.__cursor.execute(
                    "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_time_cards,
                                                                     cn=self.__column_date,
                                                                     ct=field_text));

            self.__commit();
            self.__disconnect();
            # self.__cursor.execute(
            #     'CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_mail,
            #                                                                      nf=self.__column_id,
            #                                                                      ft=field_int));
            # self.__cursor.execute(
            #     "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_mail,
            #                                                      cn=self.__column_street_address,
            #                                                      ct=field_text));
            # self.__cursor.execute(
            #     "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_mail,
            #                                                      cn=self.__column_city,
            #                                                      ct=field_text));
            # self.__cursor.execute(
            #     "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_mail,
            #                                                      cn=self.__column_state,
            #                                                      ct=field_text));
            # self.__cursor.execute(
            #     "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_mail,
            #                                                      cn=self.__column_zip_code,
            #                                                      ct=field_text));
            #
            # self.__cursor.execute(
            #     'CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_direct_deposit,
            #                                                                      nf=self.__column_id,
            #                                                                      ft=field_int));
            # self.__cursor.execute(
            #     "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_direct_deposit,
            #                                                      cn=self.__column_account_number,
            #                                                      ct=field_text));
            # self.__cursor.execute(
            #     "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_direct_deposit,
            #                                                      cn=self.__column_routing_number,
            #                                                      ct=field_text));
            #
            # self.__cursor.execute(
            #     'CREATE TABLE IF NOT EXISTS {tn} ({nf} {ft} PRIMARY KEY)'.format(tn=self.__table_pick_up,
            #                                                                      nf=self.__column_id,
            #                                                                      ft=field_int));
            # self.__cursor.execute(
            #     "ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}".format(tn=self.__table_pick_up,
            #                                                      cn=self.__column_post_master,
            #                                                      ct=field_text));


    # def insert_employee(self, id, first_name, last_name, union_dues, type, payment_method):
    #     self.__connect();
    #
    #     param = [];
    #     param.extend((id, first_name, last_name, union_dues, type, payment_method));
    #     try:
    #         self.__cursor.execute(
    #             "INSERT INTO {tn} ({id}, {fname}, {lname}, {union}, {type},{pay_meth}) VALUES(?, ?, ?, ?, ?, ?)"
    #                 .format(tn=self.__table_employees,
    #                         id=self.__column_id,
    #                         fname=self.__column_first_name,
    #                         lname=self.__column_last_name,
    #                         type=self.__column_type,
    #                         union=self.__column_union_dues,
    #                         pay_meth=self.__column_payment_method), param);
    #     except:
    #         print("Error");
    #
    #     self.__commit();
    #     self.__disconnect();
    #
    # def get_employee(self, id):
    #     self.__connect();
    #     param = [];
    #     param.append(id);
    #
    #     self.__cursor.execute(
    #         "SELECT {fname}, {lname} FROM {tn} WHERE {id} = ?"
    #             .format(fname=self.__column_first_name,
    #                     lname=self.__column_last_name,
    #                     tn=self.__table_employees,
    #                     id=self.__column_id), param);
    #
    #     result = self.__cursor.fetchall();
    #
    #     self.__disconnect();
    #     return result;
    #
    # def get_all_employees(self):
    #     self.__connect();
    #
    #     self.__cursor.execute(
    #         "SELECT {id}, {fname}, {lname} FROM {tn}"
    #             .format(id=self.__column_id,
    #                     fname=self.__column_first_name,
    #                     lname=self.__column_last_name,
    #                     tn=self.__table_employees));
    #
    #     result = self.__cursor.fetchall();
    #
    #     self.__disconnect();
    #     return result;

    def insert_hourly_employee(self, id, last_name, first_name, rate, union_dues, payment_method):
        self.__connect();
        param = [];
        param.extend((id, last_name, first_name, rate, union_dues, payment_method));

        self.__cursor.execute(
            "INSERT INTO {tn} ({id}, {lname}, {fname}, {rate}, {union}, {method}) VALUES(?, ?, ?, ?, ?, ?)"
                .format(tn=self.__table_hourly_employees,
                        id=self.__column_id,
                        lname=self.__column_last_name,
                        fname= self.__column_first_name,
                        rate=self.__column_rate,
                        union=self.__column_union_dues,
                        method=self.__column_payment_method), param);

        self.__commit();
        self.__disconnect();

    def insert_salary_employee(self, id, last_name, first_name, salary, commission, union_dues, payment_method):
        self.__connect();
        param = [];
        param.extend((id, last_name, first_name, salary, commission, union_dues, payment_method));

        self.__cursor.execute(
            "INSERT INTO {tn} ({id}, {lname}, {fname}, {salary}, {comm}, {union}, {method}) VALUES(?, ?, ?, ?, ?, ?, ?)"
                .format(tn=self.__table_salaried_employees,
                        id=self.__column_id,
                        lname=self.__column_last_name,
                        fname= self.__column_first_name,
                        salary=self.__column_salary,
                        comm=self.__column_commission,
                        union=self.__column_union_dues,
                        method=self.__column_payment_method), param);


        self.__commit();
        self.__disconnect();

    # def insert_mail(self, id, street_address, city, state, zip_code):
    #     self.__connect();
    #     param = [];
    #     param.extend((id, street_address, city, state, zip_code));
    #
    #     self.__cursor.execute(
    #         "INSERT INTO {tn} ({id}, {street}, {city}, {state}, {zip}) VALUES(?, ?, ?, ?, ?)"
    #             .format(tn=self.__table_mail,
    #                     id=self.__column_id,
    #                     street=self.__column_street_address,
    #                     city=self.__column_city,
    #                     state=self.__column_state,
    #                     zip=self.__column_zip_code), param);
    #
    #     self.__commit();
    #     self.__disconnect();
    #
    # def insert_direct_deposit(self, id, account, routing):
    #     self.__connect();
    #     param = [];
    #     param.extend((id, account, routing));
    #
    #     self.__cursor.execute(
    #         "INSERT INTO {tn} ({id}, {account}, {routing}) VALUES(?, ?, ?)"
    #             .format(tn=self.__table_direct_deposit,
    #                     id=self.__column_id,
    #                     account=self.__column_account_number,
    #                     routing=self.__column_routing_number), param);
    #
    #     self.__commit();
    #     self.__disconnect();
    #
    # def insert_pick_up(self, id):
    #     self.__connect();
    #     pickup = "Post Master";
    #     param = [];
    #     param.extend((id, pickup));
    #
    #     self.__cursor.execute(
    #         "INSERT INTO {tn} ({id}, {pickup}) VALUES(?, ?)"
    #             .format(tn=self.__table_pick_up,
    #                     id=self.__column_id,
    #                     pickup=self.__column_post_master), param);
    #
    #     self.__commit();
    #     self.__disconnect();