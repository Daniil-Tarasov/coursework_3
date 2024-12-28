from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def load_employers(self, keyword):
        pass

    @abstractmethod
    def load_vacancies_by_id(self, id_employer):
        pass
