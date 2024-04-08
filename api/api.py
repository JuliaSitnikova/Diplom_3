import requests
import allure
from constants import Constants

class BaseRequests:
    host = Constants.MAIN_PAGE_URL

    def post_request(self, url, data):
        response = requests.post(url=url, data=data)
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text

    def delete_request(self, url, token):
        headers = {"Content-Type": "application/json", 'authorization': token}
        response = requests.delete(url=url, headers=headers)
        if 'application/json' in response.headers['Content-Type']:
            return response.json()
        else:
            return response.text


class UserRequests(BaseRequests):
    user_handler = 'api/auth/register'
    manipulate_user_handler = 'api/auth/user'

    @allure.step('Создание пользователя через запрос POST')
    def post_create_user(self, data=None):
        url = f"{self.host}{self.user_handler}"
        return self.post_request(url, data=data)

    @allure.step('Удаление пользователя через запрос DELETE')
    def delete_user(self, token=None):
        url = f"{self.host}{self.manipulate_user_handler}"
        return self.delete_request(url, token=token)