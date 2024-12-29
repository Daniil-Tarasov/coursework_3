def get_data_employer_by_id(employers: list, user_id: str):
    """Функция выбирает работодателя из списка по ID"""

    employers_list = []

    for employer in employers:
        if employer["employer_id"] == user_id:
            employers_list.append(
                {
                    "employer_id": employer['employer_id'],
                    "employer_name": employer['employer_name'],
                    "employer_url": employer.get("employer_url"),
                    'open_vacancies': employer['open_vacancies']
                }
            )
    return employers_list


test_list = [{'employer_id': '9498112', 'employer_name': 'Яндекс Крауд', 'employer_url': 'https://api.hh.ru/employers/9498112', 'open_vacancies': 3625}, {'employer_id': '1740', 'employer_name': 'Яндекс', 'employer_url': 'https://api.hh.ru/employers/1740', 'open_vacancies': 1026}, {'employer_id': '9498120', 'employer_name': 'Яндекс Команда для бизнеса', 'employer_url': 'https://api.hh.ru/employers/9498120', 'open_vacancies': 631}, {'employer_id': '9694561', 'employer_name': 'Яндекс.Еда', 'employer_url': 'https://api.hh.ru/employers/9694561', 'open_vacancies': 458}, {'employer_id': '5008932', 'employer_name': 'Яндекс Практикум', 'employer_url': 'https://api.hh.ru/employers/5008932', 'open_vacancies': 35}, {'employer_id': '10571093', 'employer_name': 'Яндекс.Доставка', 'employer_url': 'https://api.hh.ru/employers/10571093', 'open_vacancies': 1}, {'employer_id': '11637308', 'employer_name': 'Партнер сервиса Яндекс доставка', 'employer_url': 'https://api.hh.ru/employers/11637308', 'open_vacancies': 1}, {'employer_id': '2532295', 'employer_name': 'Официальный партнер Яндекс такси ИП Galaxy', 'employer_url': 'https://api.hh.ru/employers/2532295', 'open_vacancies': 0}, {'employer_id': '2564113', 'employer_name': 'Yandex-taxi (ТОО Dalal)', 'employer_url': 'https://api.hh.ru/employers/2564113', 'open_vacancies': 0}, {'employer_id': '3068215', 'employer_name': 'Яндекс Такси (ИП Кондратьев)', 'employer_url': 'https://api.hh.ru/employers/3068215', 'open_vacancies': 0}]

if __name__ == "__main__":
    print(get_data_employer_by_id(test_list, "1740"))
