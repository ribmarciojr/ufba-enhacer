import os
import psycopg2

from src.config.environment import settings

def postgres_conn():
    with psycopg2.connect(
        host=settings.postgres.host,
        port=settings.postgres.port,
        user=settings.postgres.user,
        password=settings.postgres.password,
        dbname=settings.postgres.name
    ) as conn:
        return conn

    
def insert_disciplina():
    return """
    INSERT INTO disciplines (code, name, workload, department, program, objective, content, bibliography)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

def get_all_disciplinas():
    return """SELECT * FROM disciplinas"""