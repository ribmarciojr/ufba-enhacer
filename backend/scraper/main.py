import datetime
import time
from pprint import pprint
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from src.interfaces.driver import Driver
from src.utils.xpaths import Login as login, Disciplinas

start = datetime.datetime.now()
driver = Driver()

driver.get(login.URL)

cpf = driver.find_element(login.CPF, 10, EC.element_to_be_clickable)
cpf.send_keys('CPF AQUI')

password = driver.find_element(login.PASS, 10, EC.element_to_be_clickable)
password.send_keys('PASSWORD AQUI')

driver.find_element(login.LOGIN_BUTTON, 10, EC.element_to_be_clickable).click()

driver.get(Disciplinas.URL)

materias = []

table = driver.find_element(Disciplinas.TABLE, 10, EC.presence_of_element_located)
tbody = table.find_element(By.TAG_NAME, 'tbody')
lines = tbody.find_elements(By.TAG_NAME, 'tr')

for line in lines:
    checker = line.find_elements(By.TAG_NAME, 'td')[0]
    if not checker.get_attribute('colspan'):
        if checker.text:
            semestre = checker.text

        natureza = line.find_elements(By.TAG_NAME, 'td')[1].text
        code = line.find_elements(By.TAG_NAME, 'td')[2].text
        nome = line.find_elements(By.TAG_NAME, 'td')[3].text
        pre_req = line.find_elements(By.TAG_NAME, 'td')[4].text.replace(',', ', ')

        materia = {'Nome': nome, 'Código': code, 'Natureza': natureza, 'Semestre': semestre, 'Pré requisitos': pre_req}
        materias.append(materia)

end = datetime.datetime.now() - start
print(end)

pprint(materias)

