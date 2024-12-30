from config.config import config
from src.bdmanager import DBManager
from src.create_and_rec_db import create_bd, record_data_in_db
from src.hh_api import HHApi
from src.utils import get_data_employer_by_id
from src.vacancies import Vacancies


vacancies = []


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    global vacancies

    user_employers = []
    answer = ""
    default_name = "employers"

    params = config()

    print("Здравствуйте, пользователь!")
    while answer.lower() != "n":
        print("Яндекс\nТ-банк\nGoogle\nСБЕР\nSkypro\nХ5 Group\nVK\nApple\nMicrosoft\nNVIDIA")
        query = input("Введите название компании по которой желаете получить данные или скопируйте из списка сверху: ")
        if query:
            hh = HHApi()
            employers = hh.load_employers(query) # поиск работодателей в hh по запросу пользователя
            hh = HHApi()
            user_id = input("Вставьте ID компании, для поиска вакансий ")
            user_employer = get_data_employer_by_id(employers, user_id) # получаем нужную компанию
            user_employers.extend(user_employer)
            vacancies_list = hh.load_vacancies_by_id(user_id) # получаем список вакансий по ID компании
            vacancies = Vacancies.get_vacancies_from_list(vacancies_list) # записываем вакансии в класс Vacancies
        else:
            print("Не оставляйте поле пустым")
        answer = input("Желаете выполнить поиск ещё раз? y/n ")
        while answer.lower() not in ['y', 'n']:
            answer = input("Введите либо 'y' либо 'n' ")

    db_name_user = input("Задайте имя для базы данных или оставьте по умолчанию(employers) ")

    if db_name_user:
        db_name = db_name_user
    else:
        db_name = default_name

    create_bd(db_name, params) # создаём базу данных
    record_data_in_db(user_employers, vacancies, db_name, params) # запись данных в таблицы

    while True:
        options = input(
            """Выберете одну из опций:
            1 - Вывести все компании с количеством вакансий в них;
            2 - Вывести все вакансии;
            3 - Вывести среднюю зарплату по вакансиям;
            4 - Вывести вакансии с заработной платой выше среднего;
            5 - Вывести вакансии по ключевому слову;
            6 - Завершить работу\n
            """
        )
        db_manager = DBManager(db_name, params)
        if options == "1":
            db_manager.get_companies_and_vacancies_count()
        elif options == "2":
            db_manager.get_all_vacancies()
        elif options == "3":
            db_manager.get_avg_salary()
        elif options == "4":
            db_manager.get_vacancies_with_higher_salary()
        elif options == "5":
            keyword = input("Введите ключевое слово для поиска ")
            db_manager.get_vacancies_with_keyword(keyword)
        elif options == "6":
            print("Работа завершена.")
            break
        else:
            print("Введён некорректный номер. Пожалуйста, введите число от 1 до 6: ")


# if __name__ == "__main__":
#     user_interaction()
