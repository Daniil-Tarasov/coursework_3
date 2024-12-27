from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def load_vacancies(self, keyword):
        pass
