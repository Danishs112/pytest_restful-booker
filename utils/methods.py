import requests
from utils.assertions import Assertions


class Methods:
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    cookie = ""

    """ GET Method"""
    @staticmethod
    def get(url):
        result = requests.get(url, headers=Methods.headers, cookies=Methods.cookie)
        Assertions.check_status_code(result,200)
        return result

    """ POST Method """
    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        Assertions.check_status_code(result, 200)
        return result

    """ PATCH Methods"""
    @staticmethod
    def patch(url, body, headers):
        result = requests.patch(url, json=body, headers=headers, cookies=Methods.cookie)
        Assertions.check_status_code(result, 200)
        return result

    """ DELETE Methods"""
    @staticmethod
    def delete(url, headers):
        result = requests.delete(url, headers=headers, cookies=Methods.cookie)
        Assertions.check_status_code(result, 201)
        return result