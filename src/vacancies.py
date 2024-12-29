class Vacancies:
    """Класс для работы с вакансиями"""

    __list_vacancies = []

    def __init__(
        self,
        vacancy_id: int | str,
        name: str,
        url: str,
        salary: dict,
        responsibility: str = "Описание не указано",
        requirements: str = "Требования не указаны",
    ):
        """Конструктор класса"""

        self.__vacancy_id = vacancy_id
        self.__name = name
        self.__url = url
        self.__salary = self.__validate_salary(salary)
        self.__responsibility = responsibility
        self.__requirements = requirements
        dict_vacancy = {
            "ID": self.__vacancy_id,
            "name": self.__name,
            "url": self.__url,
            "salary": self.__salary,
            "responsibility": self.__responsibility,
            "requirements": self.requirements,
        }
        self.__list_vacancies.append(dict_vacancy)

    @classmethod
    def get_vacancies_from_list(cls, vacancies_list: list) -> list:
        """Получение вакансий из списка"""

        for vacancy in vacancies_list:
            vacancy_id = vacancy.get('id')
            url = vacancy.get("url") if vacancy.get("url") else vacancy.get("alternate_url")
            salary = vacancy.get("salary")
            responsibility = vacancy["snippet"].get("responsibility", "Обязанности не указаны")
            requirements = vacancy["snippet"].get("requirements", "Требования не указаны")

            cls(
                vacancy_id=vacancy_id,
                name=vacancy.get("name", "Не указано"),
                url=url,
                salary=salary,
                responsibility=responsibility if responsibility is not None else "Не указано",
                requirements=requirements,
            )
        return cls.__list_vacancies

    @staticmethod
    def __validate_salary(salary: dict) -> None | int:
        """Метод валидации зарплаты"""

        if salary is None or salary == "Зарплата не указана":
            return None
        else:
            salary = (salary.get("from", 0) + salary.get("to", 0)) // 2
            return salary

    def __str__(self) -> str:
        return (
            f"{self.__name} - {self.__url}. Зарплата: {self.__salary}. Описание: {self.__responsibility}. "
            f"Требования: {self.__requirements}."
        )

    @classmethod
    def list_vacancies(cls):
        """Метод для получения всех вакансий"""

        return cls.__list_vacancies

    @classmethod
    def clear_list(cls):
        cls.__list_vacancies = []

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def responsibility(self):
        return self.__responsibility

    @property
    def requirements(self):
        return self.__requirements


# if __name__ == "__main__":
#     vac1 = Vacancies("Тестировщик", "https://api.hh.ru/areas/26", {"from": 0, "to": 0, "currency": "RUB"}, "Какое-то описание", "Какие-то требования")
#     print(vac1)
#     vac2 = Vacancies.get_vacancies_from_list(
#         [
#             {
#                 "id": 12354,
#                 "name": "ert0",
#                 "url": "trhght",
#                 "salary": {"from": 1, "to": 5},
#                 "snippet": {"responsibility": "tes", "requirements": "kjh"}
#             }
#         ]
#     )
#     print(vac2)
