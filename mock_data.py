import random

GOOD = {
    'Название': 'Ваза хрустальная',
    'Описание': 'Ваза в отличном состоянии, бережного пользования, красиво смотрится в светлом интерьере',
    'Стоимость': 1578,
    'Категория': 'Садоводство',
    'Город': 'Казань',
    'Состояние товара': 'Б/У'
}

EXISTING_ACC = {
    'email': 'qayp.egor.1767612509@autotest.local',
    'password': 'V7@qL9!T$2ZpH#8NfXK'
}


INVALID_EMAIL = 'bad_email'
VALID_PASSWORD = 'Password123'


def generate_email():
    return f'user_{random.randint(100000, 999999)}@mail.ru'
