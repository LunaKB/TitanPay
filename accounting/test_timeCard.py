from unittest import TestCase
from accounting.time_card import TimeCard
from datetime import datetime


class TestTimeCard(TestCase):
    def test_get_date(self):
        test_time_card = TimeCard(datetime.now().date(), datetime.now().time())
        self.assertEquals(datetime.now().date(), test_time_card.get_date())

    def test_get_end_time(self):
        test_time_card = TimeCard(datetime.now().date(), datetime.now().time())
        self.assertEquals(datetime.now().date(), test_time_card.get_end_time())

    def test_set_end_time(self):
        test_time_card = TimeCard(datetime.now().date(), datetime.now().time())
        test_time_card.set_end_time(datetime.now().time())
        self.assertEquals(datetime.now().date(), test_time_card.get_end_time())

    def test_calculate_daily_pay(self):
        test_time_card = TimeCard(datetime.now().date(), datetime.now().time())
        test_time_card.set_end_time(datetime.now().time() + 7)
        self.assertEquals(7, test_time_card.calculate_daily_pay(1))
