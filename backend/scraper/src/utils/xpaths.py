class Login:
    URL = 'https://siac.ufba.br/'
    CPF = '/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[1]/td/font[2]/input'
    PASS = '/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[2]/td/font[2]/input'
    LOGIN_BUTTON = '/html/body/table/tbody/tr[2]/td[2]/form/table/tbody/tr[4]/td/input'
    LOGIN_VALIDATION = '//*[normalize-space() = "Página Inicial"]'

class Disciplines:
    class Course:
        URL = 'https://siac.ufba.br/SiacWWW/ListarCursosGrade.do?cdGrauCurso=01'
        TABLE = '/html/body/table/tbody/tr[3]/td[2]/center[2]/table'
        OBLIGATEDS = '/html/body/table/tbody/tr[3]/td[2]/div[1]/a[1]'

    URL = 'https://siac.ufba.br/SiacWWW/ConsultarDisciplinasObrigatoriasInterno.do'
    TABLE = '/html/body/table/tbody/tr[3]/td[2]/center[1]/table'
    WORKLOAD = '/html/body/table/tbody/tr[3]/td[2]/center[2]/table/tbody/tr[5]'
    PROGRAM = '/html/body/table/tbody/tr[3]/td[2]/center[2]/table/tbody/tr[7]/td'
    OBJECTIVES = '/html/body/table/tbody/tr[3]/td[2]/center[2]/table/tbody/tr[10]/td'
    CONTENT = '/html/body/table/tbody/tr[3]/td[2]/center[2]/table/tbody/tr[12]/td'
    BIBLIOGRAPHY = '/html/body/table/tbody/tr[3]/td[2]/center[2]/table/tbody/tr[14]/td'
    
    