import tkinter

class MainScreen:
    
    def __init__(self):
        
        self.main_window = tkinter.Tk();

        self.row1 = tkinter.Frame(self.main_window);
        self.row1.pack(padx = 2, pady = 2);

        self.first_name = tkinter.LabelFrame(self.row1, text = "First Name", bd = 0, padx = 2);
        self.first_name.pack(side = 'left', padx = 2, pady = 2);

        self.first_name_entry = tkinter.Entry(self.first_name, width = 20);
        self.first_name_entry.pack(padx = 2, pady = 2);

        self.last_name = tkinter.LabelFrame(self.row1, text = "Last Name", bd = 0, padx = 2);
        self.last_name.pack(side = 'left', padx = 2, pady = 2);

        self.last_name_entry = tkinter.Entry(self.last_name, width = 20);
        self.last_name_entry.pack(padx = 2, pady = 2);

        self.employee_id = tkinter.LabelFrame(self.row1, text = "Employee ID", bd = 0, padx = 2);
        self.employee_id.pack(side = 'left', padx = 2, pady = 2);

        self.employee_id_entry = tkinter.Entry(self.employee_id, width = 20);
        self.employee_id_entry.pack(padx = 2, pady = 2);

        self.row2 = tkinter.Frame(self.main_window);
        self.row2.pack(padx = 2, pady = 2)

        self.employee_type_label = tkinter.Label(self.row2, text = "Employee Type: ");
        self.employee_type_label.pack(side = 'left', padx = 2, pady = 2);

        self.radio_var1 = tkinter.IntVar()
        self.radio_var1.set(1)

        self.hourly_rbutton = tkinter.Radiobutton(self.row2, text = 'Hourly', variable = self.radio_var1, value = 1);
        self.hourly_rbutton.pack(side='left', padx = 2, pady = 2);

        self.salary_rbutton = tkinter.Radiobutton(self.row2, text = 'Salary', variable = self.radio_var1, value = 2);
        self.salary_rbutton.pack(side = 'left', padx = 2, pady = 2);

        self.union_dues_label = tkinter.Label(self.row2, text = '|  Union Dues:');
        self.union_dues_label.pack(side = 'left', padx = 2, pady = 2);

        self.union_dues_entry = tkinter.Entry(self.row2, width = 10);
        self.union_dues_entry.pack(side = 'left', padx = 2, pady = 2);

        self.row3 = tkinter.Frame(self.main_window);
        self.row3.pack(padx = 2, pady = 2);

        self.hourly_rate = tkinter.LabelFrame(self.row3, text = "Hourly Rate", bd = 0, padx = 2);
        self.hourly_rate.pack(side = 'left', padx = 2, pady = 2);

        self.hourly_rate_entry = tkinter.Entry(self.hourly_rate, width = 15);
        self.hourly_rate_entry.pack(padx = 2, pady = 2);

        self.display_timecards = tkinter.Button(self.row3, text = "Display Time Cards", height = 2);
        self.display_timecards.pack(side = 'left', padx = 2, pady = 2);

        self.salary = tkinter.LabelFrame(self.row3, text = "Salary", bd = 0, padx = 2);
        self.salary.pack(side = 'left', padx = 2, pady = 2);

        self.salary_entry = tkinter.Entry(self.salary, width = 15);
        self.salary_entry.pack(padx = 2, pady = 2);

        self.display_sales = tkinter.Button(self.row3, text = "Display Sales", height = 2);
        self.display_sales.pack(side = 'left', padx = 2, pady = 2);   

        self.row4 = tkinter.Frame(self.main_window);
        self.row4.pack(padx = 2, pady = 2);

        self.payment_method_label = tkinter.Label(self.row4, text = 'Payment Method: ');
        self.payment_method_label.pack(side = 'left', padx = 2, pady = 2);

        self.radio_var2 = tkinter.IntVar();
        self.radio_var2.set(1);

        self.mail_rbutton = tkinter.Radiobutton(self.row4, text = 'Mail', variable = self.radio_var2, value = 1);
        self.mail_rbutton.pack(side = 'left', padx = 2, pady = 2);

        self.pickup_rbutton = tkinter.Radiobutton(self.row4, text = 'Pick Up', variable = self.radio_var2, value = 2);
        self.pickup_rbutton.pack(side = 'left', padx = 2, pady = 2);

        self.deposit_rbutton = tkinter.Radiobutton(self.row4, text = 'Direct Deposit', variable = self.radio_var2, value = 3);
        self.deposit_rbutton.pack(side = 'left', padx = 2, pady = 2);

        self.row5 = tkinter.Frame(self.main_window);
        self.row5.pack();

        self.street_address = tkinter.LabelFrame(self.row5, text = 'Street Address', bd = 0, padx = 2);
        self.street_address.pack(side = 'left', padx = 2, pady = 2);

        self.street_address_entry = tkinter.Entry(self.street_address, width = 20);
        self.street_address_entry.pack(padx = 2, pady = 2);

        self.city = tkinter.LabelFrame(self.row5, text = 'City', bd = 0, padx = 2);
        self.city.pack(side = 'left', padx = 2, pady = 2);

        self.city_entry = tkinter.Entry(self.city, width = 10);
        self.city_entry.pack(padx = 2, pady = 2);

        self.state = tkinter.LabelFrame(self.row5, text = 'State', bd = 0, padx = 2);
        self.state.pack(side = 'left', padx = 2, pady = 2);

        self.state_entry = tkinter.Entry(self.state, width = 5);
        self.state_entry.pack(padx = 2, pady = 2);

        self.zip_code = tkinter.LabelFrame(self.row5, text = 'Zip Code', bd = 0, padx = 2);
        self.zip_code.pack(side = 'left', padx = 2, pady = 2);

        self.zip_code_entry = tkinter.Entry(self.zip_code, width = 10);
        self.zip_code_entry.pack(padx = 2, pady = 2);

        self.row6 = tkinter.Frame(self.main_window);
        self.row6.pack();

        self.account_number = tkinter.LabelFrame(self.row6, text = 'Account Number', bd = 0, padx = 2);
        self.account_number.pack(side = 'left', padx = 2, pady = 2);

        self.account_number_entry = tkinter.Entry(self.account_number, width = 20);
        self.account_number_entry.pack(padx = 2, pady = 2);

        self.routing_number = tkinter.LabelFrame(self.row6, text = 'Routing Number', bd = 0, padx = 2);
        self.routing_number.pack(side = 'left', padx = 2, pady = 2);

        self.routing_number_entry = tkinter.Entry(self.routing_number, width = 20);
        self.routing_number_entry.pack(padx = 2, pady = 2);

        self.row7 = tkinter.Frame(self.main_window);
        self.row7.pack(padx = 2, pady = 2);

        self.create_save_employee_button = tkinter.Button(self.row7, text = 'Create/Save Employee Record');
        self.create_save_employee_button.pack(side = 'left', padx = 2, pady = 2);

        self.edit_employee_button = tkinter.Button(self.row7, text = 'Edit Employee Record');
        self.edit_employee_button.pack(side = 'left', padx = 2, pady = 2);

        self.process_payroll_button = tkinter.Button(self.row7, text = 'Process Payroll', command = self.show_run);
        self.process_payroll_button.pack(side = 'left', padx = 2, pady = 2);
      
        tkinter.mainloop();

    def show_run(self):
        self.sub_window = tkinter.Tk();
        self.run_payroll_button = tkinter.Button(self.sub_window, text = 'Run Payroll');
        self.run_payroll_button.pack(padx = 2, pady = 2);
        

test_gui = MainScreen();
