from faker import Faker
from datetime import datetime, timedelta

class DataGenerator:
    fake = Faker()  # Create a Faker instance as a class attribute

    @staticmethod
    def first_name():
        return DataGenerator.fake.first_name()

    @staticmethod
    def last_name():
        return DataGenerator.fake.last_name()

    @staticmethod
    def get_date():
        checkin = DataGenerator.fake.date_between(start_date='today', end_date='+30d')
        checkout = checkin + timedelta(days=10)
        date = [checkin.strftime('%Y-%m-%d'), checkout.strftime('%Y-%m-%d')]
        return date