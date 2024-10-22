from utils.data_generator import DataGenerator


class TestData:

    BASE_URL = "https://restful-booker.herokuapp.com"
    USERNAME = "admin"
    PASSWORD = "password123"
    PAID_DEPOSIT1 = True
    PAID_DEPOSIT2 = False
    TOTAL_PRICE1 = 500
    TOTAL_PRICE2 = 1000
    ADDITIONAL_NEEDS1 = "lunch"
    ADDITIONAL_NEEDS2 = "no preference"
    

    def __init__(self):
        self.FIRST_NAME = self.generate_first_name()
        self.LAST_NAME = self.generate_last_name()
        self.CHECKIN_DATE = self.generate_checkin_date()
        self.CHECKOUT_DATE = self.generate_checkout_date()

    @staticmethod
    def generate_first_name():
        generator = DataGenerator()
        return generator.first_name()

    @staticmethod
    def generate_last_name():
        generator = DataGenerator()
        return generator.last_name()

    @staticmethod
    def generate_checkin_date():
        generator = DataGenerator()
        date_object = generator.get_date()
        return date_object[0]

    @staticmethod
    def generate_checkout_date():
        generator = DataGenerator()
        date_object = generator.get_date()
        return date_object[1]
