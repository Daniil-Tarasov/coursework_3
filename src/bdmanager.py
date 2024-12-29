import psycopg2


class DBManager:
    """Класс для работы с БД"""

    __slots__ = ("name", "params")

    def __init__(self, db_name, params):
        self.name = db_name
        self.params = params

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании"""

        conn = psycopg2.connect(dbname=self.name, **self.params)
        cur = conn.cursor()

        cur.execute(
            """
            SELECT employer_name, COUNT(*)
            FROM vacancies JOIN employers_list USING (employer_id)
            GROUP BY employer_name DESC;
            ORDER BY COUNT(*)
            """
        )

        rows = cur.fetchhall()
        for row in rows:
            print(f'Название вакансии: {row[0]}\nКоличество вакансий: {row[1]}\n')

        cur.close()
        conn.close()

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""

        conn = psycopg2.connect(dbname=self.name, **self.params)
        cur = conn.cursor()

        cur.execute(
            """
            SELECT employer_name, 
            vacancy_name, 
            salary, 
            vacancy_url
            FROM vacancies 
            JOIN employers_list USING (employer_id); 
            """
        )

        rows = cur.fetchhall()

        cur.close()
        conn.close()

        return rows

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""

        conn = psycopg2.connect(dbname=self.name, **self.params)
        cur = conn.cursor()

        cur.execute(
            """
            SELECT AVG(salary) AS average_salary
            FROM vacancies
            WHERE salary IS NOT NULL;
            """
        )

        rows = cur.fetchone()

        cur.close()
        conn.close()

        return round(rows[0], 2)

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""

        conn = psycopg2.connect(dbname=self.name, **self.params)
        cur = conn.cursor()

        cur.execute(
            """
            SELECT * FROM vacancies
            WHERE salary > (SELECT AVG(salary) FROM vacancies);
            """
        )

        rows = cur.fetchhall()

        cur.close()
        conn.close()

        return rows

    def get_vacancies_with_keyword(self, key_word):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова"""

        conn = psycopg2.connect(dbname=self.name, **self.params)
        cur = conn.cursor()

        cur.execute(
            """
            SELECT * FROM vacancies
            WHERE vacancy_name LIKE %s;
            """,
            (f"%{key_word.lower()}%",),
        )

        rows = cur.fetchhall()

        cur.close()
        conn.close()

        return rows
