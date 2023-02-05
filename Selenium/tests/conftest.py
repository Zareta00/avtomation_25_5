import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
# опции из хром которыми можно пользоватлься при необходимости.


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Используем 'headless' если нам не нужен UI браузера, если нужен UI 'chrome'.
    # options.add_argument('--window-size=800,600') # расширение окна
    return options  # возвращаем сами опции


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    # инициализатия драйвера Chrome с указанием пути  файлу
    driver = webdriver.Chrome(
        options=options)  # executable_path='C:\Program Files\Google\Chrome\Application\chromedriver' - путь к файлу
    return driver


@pytest.fixture(scope='function')  # 'scope=' это то как  наши тесты будут реагировать на fixture
# function - будет запускать тесты как с чистого личта
# session - сохраняет данный после тестов, накралывая их друге на друга. Не подходит для запуска тестов одновременно.
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://petfriends.skillfactory.ru'
    if request.cls is not None:  # смотрим будут ли наши тесты находиться в классе, если будут
        request.cls.driver = driver  # используем наш driver чтобы он работал в классе с нашими тестами
    driver.get(url)  # если нет, изпользуем наш driver для нахождея нашего url
    yield driver
    driver.close()  # quit чтобы закрыть все вкладки в браузере
