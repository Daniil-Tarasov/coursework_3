import requests

from src.base_api import BaseApi


class HHApi(BaseApi):
    """Класс для работы с API HeadHunter"""


    def __init__(self):
        """Конструктор класса"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"page": 0, "per_page": 10}
        self.__vacancies = []
        self.__employers = []

    def _get_response(self) -> bool:
        """Метод подключения к API"""

        response = requests.get(
            self.__url, headers=self.__headers, params=self.__params
        )
        status_code = response.status_code
        if status_code == 200:
            return True
        else:
            return False

    def load_employers(self, keyword: str):
        """Метод получения данных компаний из API сервиса"""

        if self._get_response():
            self.__params["text"] = keyword
            self.__params["sort_by"] = "by_vacancies_open"
            while self.__params.get("page") != 1:
                response = requests.get("https://api.hh.ru/employers", headers=self.__headers, params=self.__params)
                employers = response.json()["items"]
                self.__params["page"] += 1
                for emp in employers:
                    print(f'ID - {emp['id']}. Название - {emp['name']}. Открытых вакансий - {emp['open_vacancies']}')
                    self.__employers.append(
                        {
                            "employers_id": emp['id'],
                            "employer_name": emp['name'],
                            "employer_url": emp.get("url"),
                            'open_vacancies': emp['open_vacancies']
                        }
                    )
        return self.__employers

    def load_vacancies_by_id(self, id_employer: str):
        """Метод загрузки данных вакансий по ID компании из API сервиса"""

        if self._get_response():
            self.__params["employer_id"] = id_employer
            while self.__params.get("page") != 10:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1

        return self.__vacancies


# if __name__ == "__main__":
#     hh = HHApi()
#     print(hh.load_employers("Яндекс"))
    # print(hh.load_vacancies_by_id("1740"))
# 1740 - Яндекс
# 78638 - Т-банк
# 40565 - Google
# 3529 - Сбер
# 4805396 - Skypro
# 4233 - Х5 Group
# 15478 - VK
# 25870 - Apple
# 4771 - Microsoft
# 5135 - NVIDIA
