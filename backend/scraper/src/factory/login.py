import os
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from src.interfaces.driver import Driver
from src.utils.xpaths import Login as login
from src.config.environment import settings


class Login:
    def __init__(self, driver: Driver) -> None:
        self._driver = driver

    def login(self):
        user = settings.siac.user
        password = settings.siac.password
        
        print(user, password)

        
        self._driver.get(login.URL)
        time.sleep(5)

        cpf = self._driver.find_element(login.CPF, 10, EC.element_to_be_clickable)
        cpf.send_keys(user)

        password = self._driver.find_element(login.PASS, 10, EC.element_to_be_clickable)
        print(password)
        password.send_keys(password)

        self._driver.find_element(login.LOGIN_BUTTON, 10, EC.element_to_be_clickable).click()

        if not self.__validate_login():
            raise Exception('Não foi possível fazer login. Cheque as credenciais e tente novamente.')

    def __validate_login(self):
        try:
            initial_page = self._driver.find_element(login.LOGIN_VALIDATION, 10, EC.element_to_be_clickable)
            return True
        except TimeoutException:
            return False
