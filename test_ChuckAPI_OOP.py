import requests

class test_Chuck_jokes():
    """Тестируем API сайта Чака Норриса"""
    def __init__(self, category="sport"):
        self.category = category

    def test_get_category_list(self):
        """Вывод доступных категорий шуток"""
        url = "https://api.chucknorris.io/jokes/categories"
        result = requests.get(url)
        if result.status_code == 200:
            print('Status code:', result.status_code)
        else:
            print('Запрос ошибочный')
        print(result.json())

    def test_get_random_joke(self):
        url = "https://api.chucknorris.io/jokes/random"
        result = requests.get(url)
        if result.status_code == 200:
            print('Status code:', result.status_code)
        else:
            print('Запрос ошибочный')
        print(result.json())
        check_joke = result.json()
        if "Chuck" in check_joke.get('value'):
            print('Шутка про Чака подтверждена')
        else:
            print('Шутка про Чака не обнаружена')

    def test_get_joke_by_category(self):
        """Вывод шутки про Чака согласно выбранной категории (по-умолчанию - спорт)"""
        url = "https://api.chucknorris.io/jokes/random?category="+self.category
        result = requests.get(url)
        if result.status_code == 200:
            print('Status code:', result.status_code)
        else:
            print('Запрос ошибочный')
        print(result.json())
        check_joke = result.json()
        if "Chuck" in check_joke.get('value'):
            print('Шутка про Чака подтверждена')
        else:
            print('Шутка про Чака не обнаружена')

# category_list = test_Chuck_jokes()
# category_list.test_get_category_list()

# rnd_joke = test_Chuck_jokes()
# rnd_joke.test_get_random_joke()

category_joke = test_Chuck_jokes("dev")
category_joke.test_get_joke_by_category()