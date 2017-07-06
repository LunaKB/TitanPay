from unittest import TestCase
from accounting.time_card import TimeCard
import datetime;


class TestTimeCard(TestCase):
    def test_calculate_daily_pay(self):
        #arrange
        time_cards = [];
        total = 0;

        #act
        for i in range(1, 6):
            date = "6/%d/2016" %(i);
            in_time_str = "%s %s" % (date, 900);
            in_date =  datetime.datetime.strptime(in_time_str, "%m/%d/%Y %H%M");
            out_time_str = "%s %s" %(date, 1700);
            out_date = datetime.datetime.strptime(out_time_str, "%m/%d/%Y %H%M");

            time_card = TimeCard(in_date.date(), in_date.time());
            time_card.set_end_time(out_date.time());

            time_cards.append(time_card);

        #assert
        for card in time_cards:
            total += card.calculate_daily_pay(8);
        print(total);
        self.assertGreater(total, 0);