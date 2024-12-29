from config.config import config
from src.hh_api import HHApi
from src.utils import get_data_employer_by_id
from src.vacancies import Vacancies


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    user_employers = []
    answer = ""
    default_name = "employers"

    params = config()

    print("Здравствуйте, пользователь!")
    while answer.lower() != "n":
        hh = HHApi()
        print("Яндекс\nТ-банк\nGoogle\nСБЕР\nSkypro\nХ5 Group\nVK\nApple\nMicrosoft\nNVIDIA")
        query = input("Введите название компании по которой желаете получить данные или скопируйте из списка сверху: ")
        if query:
            employers = hh.load_employers(query) # поиск работодателей в hh по запросу пользователя
            print(employers)
            hh = HHApi()
            user_id = input("Вставьте ID компании, для поиска вакансий ")
            user_employer = get_data_employer_by_id(employers, user_id) # получаем нужную компанию
            user_employers.extend(user_employer)
            print(user_employers)
            vacancies = hh.load_vacancies_by_id(user_id) # получаем список вакансий по ID компании
            print(vacancies)
            vacancies = Vacancies.get_vacancies_from_list(vacancies) # записываем вакансии в класс Vacancies
            print(vacancies)
        else:
            print("Не оставляйте поле пустым")
        answer = input("Желаете выполнить поиск ещё раз? y/n ")
        while answer.lower() not in ['y', 'n']:
            answer = input("Введите либо 'y' либо 'n' ")


if __name__ == "__main__":
    user_interaction()
