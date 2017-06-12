from datetime import date, datetime;


class TimeCard:

    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def get_date(self):
        return self.__date;

    def set_end_time(self, end_time):
        self.__end_time = end_time;


    def calculate_daily_pay(self, rate):
        calculated_time = datetime.combine(date.today(), self.__end_time) - datetime.combine(date.today(), self.__start_time);
        hours_worked = (calculated_time.seconds/60)/60;

        if hours_worked <= 8:
            daily_pay = rate * hours_worked
            return daily_pay
        else:
            # The previous way of calculating overtime pay resulted in an answer that was too low.
            # This should be more accurate.
            daily_pay = (rate * 1.5) * hours_worked;
            return daily_pay
