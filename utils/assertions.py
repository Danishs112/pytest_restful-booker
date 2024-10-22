
from requests import Response

class Assertions:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code

    @staticmethod
    def compare_two_values(text1,text2):
        assert text1 == text2

    @staticmethod
    def compare_type_values(result,val):
        assert isinstance(result, val)

    @staticmethod
    def check_array_size_greater_than_zero(lst,size):
        assert len(lst) > size

