import time
from selenium.webdriver.support import expected_conditions as EC

from src.interfaces.driver import Driver
from src.factory.login import Login
from src.factory.disciplines.disciplines import Disciplines
from src.utils.xpaths import Login as login

def main():
    driver = Driver()
    login = Login(driver)
    
    
    login.login()

    driver.get(login.URL)

    disciplines = Disciplines(driver)
    disciplines.get_all_disciplines()

if __name__ == '__main__':
    main()

