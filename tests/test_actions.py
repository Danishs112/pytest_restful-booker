from utils.methods import Methods
from utils.data import TestData
from utils.assertions import Assertions
from utils.logger import logger



base_url = TestData.BASE_URL
cookie = ""  # User Token
booking1  = "" # first booking id
booking2 = "" #second booking id
headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'Cookie': cookie
}


class Actions:

    @staticmethod
    def auth_user():
        auth_object = {
            "username": TestData.USERNAME,
            "password": TestData.PASSWORD
        }
        global headers, cookie
        post_resource = "auth"
        post_url = f"{base_url}/{post_resource}"
        result_post = Methods.post(post_url, auth_object)
        check_post = result_post.json()
        token = str(check_post.get("token"))
        cookie = "token=" + token
        headers['Cookie'] = cookie
        Assertions.compare_type_values(result_post.json(),dict)
        return result_post

    @staticmethod
    def create_booking(obj):
        post_resource = "booking"
        post_url = f"{base_url}/{post_resource}"
        result_post  = Methods.post(post_url, obj) #post resource
       #print(result_post.text)
        return result_post

    @staticmethod
    def create_first_booking():
        create_object = {
            "firstname": TestData.generate_first_name(),
            "lastname": TestData.generate_last_name(),
            "totalprice": TestData.TOTAL_PRICE1,
            "depositpaid": TestData.PAID_DEPOSIT1,
            "bookingdates": {
                "checkin": TestData.generate_checkin_date(),
                "checkout": TestData.generate_checkout_date()
            },
            "additionalneeds": TestData.ADDITIONAL_NEEDS1
        }

        response_object = Actions.create_booking(create_object)
        response_data = response_object.json()
        Assertions.compare_type_values(response_data, dict)
        logger.info('CREATE first Booking -'+ response_object.text)
        print(response_object.text)
        global booking1
        booking1  = response_data["bookingid"]

    @staticmethod
    def create_second_booking():
        create_object = {
            "firstname": TestData.generate_first_name(),
            "lastname": TestData.generate_last_name(),
            "totalprice": TestData.TOTAL_PRICE2,
            "depositpaid": TestData.PAID_DEPOSIT2,
            "bookingdates": {
                "checkin": TestData.generate_checkin_date(),
                "checkout": TestData.generate_checkout_date()
            },
            "additionalneeds": TestData.ADDITIONAL_NEEDS2
        }

        response_object = Actions.create_booking(create_object)
        response_data = response_object.json()
        Assertions.compare_type_values(response_data, dict)
        logger.info('CREATE Second Booking -' + response_object.text)
        global booking2
        booking2  = response_data["bookingid"]

    @staticmethod
    def get_booking():
        get_resource = "booking"  # GET resource
        url  = f"{base_url}/{get_resource}"
        result_get = Methods.get(url)
        Assertions.check_array_size_greater_than_zero(result_get.text,0)
        logger.info('GET All Booking -' + result_get.text)
        return result_get

    @staticmethod
    def update_booking(obj,bookid):
        patch_resource = "booking"  # PATCH resource
        patch_url = f"{base_url}/{patch_resource}/{bookid}"
        result_patch = Methods.patch(patch_url,obj, headers)
        return result_patch

    @staticmethod
    def update_first_booking():
        update_obj = {
            "totalprice" :1000
        }
        response_object = Actions.update_booking(update_obj,booking1)
        Assertions.compare_type_values(response_object.json(), dict)
        logger.info('Update the  first Booking -' + response_object.text)
        print(response_object.text)

    @staticmethod
    def update_second_booking():
        update_obj = {
            "totalprice":1500
        }
        response_object = Actions.update_booking(update_obj,booking2)
        Assertions.compare_type_values(response_object.json(), dict)
        logger.info('Update the Second Booking -' + response_object.text)
        print(response_object.text)

    @staticmethod
    def delete_first_booking():
        delete_resource = "booking"  # DELETE resource
        delete_url = f"{base_url}/{delete_resource}/{booking1}"
        result_delete = Methods.delete(delete_url, headers)
        Assertions.compare_two_values(result_delete.text,"Created")
        logger.info('Delete the first Booking -' + result_delete.text)



Actions.auth_user()
Actions.create_first_booking()
Actions.create_second_booking()
Actions.get_booking()
Actions.update_first_booking()
Actions.update_second_booking()
Actions.delete_first_booking()
