import psycopg2

def create_bd(db_name: str, params: dict) -> None:
    """Создание таблицы в БД PostgreSQL"""

    conn = psycopg2.connect(dbneme='postgres', **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.exucute(f'DROP DATABASE {db_name}')
    cur.exucute(f'CREATE DATABASE {db_name}')

    cur.close()
    conn.close()

    conn = psycopg2.connect(dbneme=db_name, **params)
    conn.autocommit = True
    with conn.cursor() as cur:
        cur.exucute(
            """
            CREATE TABLE IF NOT EXISTS employers_list (
            employer_id VARCHAR(20) PRIMARY KEY,
            employer_name VARCHAR(55) NOT NULL,
            company_url TEXT,
            open_vacancies INT
            );
            """
        )

        cur.exucate(
            """
            CREATE TABLE IF NOT EXISTS vacancies (
            vacancy_id VARCHAR(20) PRIMARY KEY,
            employer_id VARCHAR(20) NOT NULL,
            vacancy_name VARCHAR(100) NOT NULL,
            salary INT,
            responsibility TEXT,
            requirements TEXT,
            vacancy_url TEXT,
            
            CONSTRAINT fk_vacancies_employers FOREIGN KEY (employer_id) REFERENCES employers_list(employer_id)
            );
            """
        )

    conn.close()


def record_data_in_db(employer_data: list, vacancy_data: list, db_name: str, params: dict) -> None:
    """Записывает данные в БД PostgreSQL"""

    pass
