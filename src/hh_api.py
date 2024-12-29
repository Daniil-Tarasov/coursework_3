import requests

from src.base_api import BaseApi


class HHApi(BaseApi):
    """Класс для работы с API HeadHunter"""

    __slots__ = ("__url", "__headers", "__params")

    def __init__(self):
        """Конструктор класса"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"page": 0, "per_page": 10}

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

        employers = []
        if self._get_response():
            self.__params["text"] = keyword
            self.__params["sort_by"] = "by_vacancies_open"
            while self.__params.get("page") != 1:
                response = requests.get("https://api.hh.ru/employers", headers=self.__headers, params=self.__params)
                data = response.json()["items"]
                self.__params["page"] += 1
                for employer in data:
                    print(f'ID - {employer['id']}. Название - {employer['name']}. Открытых вакансий - {employer['open_vacancies']}')
                    employers.append(
                        {
                            "employer_id": employer['id'],
                            "employer_name": employer['name'],
                            "employer_url": employer.get("url"),
                            'open_vacancies': employer['open_vacancies']
                        }
                    )
        return employers

    def load_vacancies_by_id(self, id_employer: str):
        """Метод загрузки данных вакансий по ID компании из API сервиса"""

        vacancies = []
        if self._get_response():
            self.__params["employer_id"] = id_employer
            while self.__params.get("page") != 10:
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                data = response.json()["items"]
                vacancies.extend(data)
                self.__params["page"] += 1

        return vacancies


if __name__ == "__main__":
    hh = HHApi()
    print(hh.load_employers("Яндекс"))
    print(hh.load_vacancies_by_id("1740"))
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
