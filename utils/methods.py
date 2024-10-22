import requests
from utils.assertions import Assertions


class Methods:
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    cookie = ""

    """ GET Method"""
    @staticmethod
    def get(url):
   #     Logger.add_request(url, method="GET")
        result = requests.get(url, headers=Methods.headers, cookies=Methods.cookie)
        #print("getall",result.text)
        Assertions.check_status_code(result,200)
       #Logger.add_response(result)
        return result

    """ POST Method """
    @staticmethod
    def post(url, body):
    #    Logger.add_request(url, method="POST")
        result = requests.post(url, json=body, headers=Methods.headers, cookies=Methods.cookie)
        Assertions.check_status_code(result, 200)
     #   Logger.add_response(result)
        return result

    """ PATCH Methods"""
    @staticmethod
    def patch(url, body, headers):
      #  Logger.add_request(url, method="PATCH")
        result = requests.patch(url, json=body, headers=headers, cookies=Methods.cookie)
        Assertions.check_status_code(result, 200)
   #    print(
      #    Logger.add_response(result)
        return result

    """ DELETE Methods"""
    @staticmethod
    def delete(url, headers):
        result = requests.delete(url, headers=headers, cookies=Methods.cookie)
        Assertions.check_status_code(result, 201)
        return result