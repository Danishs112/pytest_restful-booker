from faker import Faker
from datetime import datetime,timedelta

class DataGenerator:

    def __init__(self, seed=None):
        if  seed is not None:
            Faker.seed(seed)
        self.fake = Faker()


    def first_name(self):
        return self.fake.first_name()

    def last_name(self):
        return self.fake.last_name()

    def get_date(self):
        checkin = self.fake.date_between(start_date='today', end_date='+30d')
        checkout = checkin + timedelta(days=10)
        date = [checkin.strftime('%Y-%m-%d'), checkout.strftime('%Y-%m-%d')]
        return date