class TimeCard:

    def __init__(self, date, start_time, end_time):
        self.__date = date
        self.__start_time = start_time
        self.__end_time = end_time

    def calculate_daily_pay(self, rate):
        self.__rate = rate
        self.__hours_worked = self.__end_time - self.__start_time

        if self.__hours_worked <= 8:
            self.__daily_pay = self.__rate * self.__hours_worked
            return self.__daily_pay
        else:
            self.__daily_pay = (8 * self.__rate) + (self.__hours_worked - 8) * 1.5 * self.__rate
            return self.__daily_pay

if __name__ == "__main__":
    test_time_card = TimeCard('05/29/2017', 8, 10)
    print(test_time_card.calculate_daily_pay(10))