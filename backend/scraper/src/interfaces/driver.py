from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import *

class Driver:
    def __init__(self):
        self.__driver = self.__build_driver()

    def get(self, url):
        self.__driver.get(url)

    def get_active_element(self):
        active_element = self.__driver.switch_to.active_element
        return active_element

    def find_element(self, value: str, timeout: float, expected_condition: callable):
        WebDriverWait(self.__driver, timeout).until(expected_condition((By.XPATH, value)))
        element = self.__driver.find_element(By.XPATH, value)
        return element

    def __build_driver(self):
        try:
            options = Options()
            # options.add_argument('--headless')
            options.add_argument('--window-size=1920,1080')
            driver = Chrome(options=options)
            driver.maximize_window()
        except:
            return self.__build_driver()
        return driver
    
    def back(self):
        self.__driver.back()