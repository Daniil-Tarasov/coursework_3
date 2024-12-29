from config.config import config
from src.hh_api import HHApi


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    user_employers = []
    answer = ""
    default_name = "employers"

    params = config()
    hh = HHApi()

    print("Здравствуйте, пользователь!")
    while answer.lower() != "n":
        print("Яндекс\nТ-банк\nGoogle\nСБЕР\nSkypro\nХ5 Group\nVK\nApple\nMicrosoft\nNVIDIA")
        query = input("Введите название компании по которой желаете получить данные или скопируйте из списка сверху: ")
        if query:
            employers = hh.load_employers(query) # поиск работодателей в hh по запросу пользователя
        else:
            print("Не оставляйте поле пустым")
        answer = input("Желаете выполнить поиск ещё раз? y/n ")
        while answer.lower() not in ['y', 'n']:
            answer = input("Введите либо 'y' либо 'n' ")


if __name__ == "__main__":
    user_interaction()
