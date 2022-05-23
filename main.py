
import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    " corrosion_protection", "postgres", "qwerty", "127.0.0.1", "5432"
)

''' Вставка данных в бд'''

violation = ('УКЗ №2', 'Обрыв анодной ВЛ')
violation_record = ", ".join(["%s"] * len(violation))

insert_query = ( f'INSERT INTO apk(equipment, text_violation) VALUES({violation_record})')

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, violation)