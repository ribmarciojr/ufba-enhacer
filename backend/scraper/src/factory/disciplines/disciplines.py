import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from psycopg2.errors import UniqueViolation

from src.interfaces.driver import Driver
from src.utils.xpaths import Disciplines as vars
from src.models.discipline import Discipline
from src.db.database import postgres_conn, insert_disciplina


class Disciplines:
    def __init__(self, driver: Driver) -> None:
        self._driver = driver

    def get_all_disciplines(self):
        self.__access_course()

    def __access_discipline(self):
        conn = postgres_conn()
        cursor = conn.cursor()
        sql = insert_disciplina()

        table = self._driver.find_element(vars.TABLE, 10, EC.presence_of_element_located)
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        lines = tbody.find_elements(By.TAG_NAME, 'tr')

        for line in lines[2:]:
            checker = line.find_elements(By.TAG_NAME, 'td')[0]
            if not checker.get_attribute('colspan'):
                name = line.find_elements(By.TAG_NAME, 'td')[3].text
                code = line.find_elements(By.TAG_NAME, 'td')[2].text
                line.find_elements(By.TAG_NAME, 'td')[3].find_element(By.TAG_NAME, 'a').click()
                discipline = self.__extract_discipline_info(name, code)
                try: 
                    cursor.execute(sql, (
                        discipline.code,
                        discipline.name,
                        discipline.workload,
                        discipline.department,
                        discipline.program,
                        discipline.objective,
                        discipline.content,
                        discipline.bibliography
                    ))
                    conn.commit()
                except UniqueViolation:
                    conn.commit()

                self._driver.back()
        
        self._driver.back()
        self._driver.back()

        cursor.close()
        conn.close()
                
        

    def __access_course(self):
        self._driver.get(vars.Course.URL)
        table = self._driver.find_element(vars.Course.TABLE, 10, EC.presence_of_element_located)
        tbody = table.find_element(By.TAG_NAME, 'tbody')
        lines = tbody.find_elements(By.TAG_NAME, 'tr')

        for line in lines[1:]:
            line.find_elements(By.TAG_NAME, 'td')[1].find_element(By.TAG_NAME, 'a').click()
            self._driver.find_element(vars.Course.OBLIGATEDS, 10, EC.element_to_be_clickable).click()

            self.__access_discipline()
    
    def __extract_discipline_info(self, name: str, code: str):
        wl_row = self._driver.find_element(vars.WORKLOAD, 10, EC.presence_of_element_located)
        return Discipline(
            code=code,
            name=name,
            workload=self.__extract_workload(wl_row),
            department=self.__extract_department(wl_row),
            program=self.__extract_program(),
            objective=self.__extract_objectives(),
            content=self.__extract_content(),
            bibliography=self.__extract_bibliography()
        )
        

    def __extract_workload(self, wl_row):
        columns = wl_row.find_elements(By.TAG_NAME, 'td')
        workload = 0
        for i in range(2):
            workload += int(columns[i].text)
        
        return workload
    
    def __extract_department(self, wl_row):
        columns = wl_row.find_elements(By.TAG_NAME, 'td')
        return columns[3].text
    
    def __extract_program(self):
        return self._driver.find_element(vars.PROGRAM, 10, EC.presence_of_element_located).text

    def __extract_objectives(self):
        return self._driver.find_element(vars.OBJECTIVES, 10, EC.presence_of_element_located).text
    
    def __extract_content(self):
        return self._driver.find_element(vars.CONTENT, 10, EC.presence_of_element_located).text
    
    def __extract_bibliography(self):
        return self._driver.find_element(vars.BIBLIOGRAPHY, 10, EC.presence_of_element_located).text