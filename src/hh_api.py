import requests

from src.base_api import BaseApi


class HHApi(BaseApi):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        """Конструктор класса"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    # def load_vacancies(self, keyword: str) -> list:
    #     """Метод загрузки данных вакансий из API сервиса"""
    #
    #     self.__params["text"] = keyword
    #     while self.__params.get("page") != 20:
    #         response = requests.get(self.__url, headers=self.__headers, params=self.__params)
    #         vacancies = response.json()["items"]
    #         self.__vacancies.extend(vacancies)
    #         self.__params["page"] += 1
    #
    #     return self.__vacancies


# if __name__ == "__main__":
#     hh = HHApi(file_worker="../data/vacancies.json")
#     print(hh.load_vacancies("Тестировщик"))
