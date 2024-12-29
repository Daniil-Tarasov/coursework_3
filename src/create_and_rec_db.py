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
            employer_id VARCHAR(20) NOT NULL,
            vacancy_id VARCHAR(20) PRIMARY KEY,
            vacancy_name VARCHAR(100) NOT NULL,
            salary TEXT,
            responsibility TEXT,
            requirements TEXT,
            vacancy_url TEXT,
            
            CONSTRAINT fk_vacancies_employers FOREIGN KEY (employer_id) REFERENCES employers_list(employer_id)
            );
            """
        )

    conn.commit()
    conn.close()


def record_data_in_db(employer_data: list, vacancy_data: list, db_name: str, params: dict) -> None:
    """Записывает данные в БД PostgreSQL"""

    conn = None
    try:
        conn = psycopg2.connect(dbname=db_name, **params)
        conn.autocommit = True
        with conn.cursor() as cur:
            for employer in employer_data:
                cur.execute(
                    """
                    INSERT INTO employers_list (employer_id, employer_name, company_url, open_vacancies)
                    VALUES (%s, %s, %s, %s)
                    RETURNING employer_id
                    """,
                    (
                        employer["employer_id"],
                        employer["employer_name"],
                        employer["employer_url"],
                        employer["open_vacancies"]
                    ),
                )
                employer_id = cur.fetchone()[0]
                for vacancy in vacancy_data:
                    cur.execute(
                        """
                        INSERT INTO vacancies (employer_id, vacancy_id, vacancy_name, salary, responsibility, requirements, vacancy_url)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        (
                            employer_id,
                            vacancy["id"],
                            vacancy["name"],
                            vacancy["salary"],
                            vacancy["responsibility"],
                            vacancy["requirements"],
                            vacancy["url"]
                        ),
                    )
            print("Таблицы заполнены")
    except Exception as ex:
        print(f'Ошибка записи данных в БД: {ex}')
    finally:
        if conn:
            conn.commit()
            conn.close()
