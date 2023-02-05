import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures('setup')
class TestLog:

    def test_log(self):
        # Найти кнопку 'Зарегистрироваться', нажать
        self.driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-success"]').click()

        # Найти конпку-ссылку 'У меня уже есть аккаунт', нажать
        self.driver.find_element(By.LINK_TEXT, 'У меня уже есть аккаунт').click()

        # Найти элемент 'email', ввести email
        self.driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('skillfac@bk.ru')

        # Найти элемент 'pass', ввести пароль
        self.driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys('YpaipiPZA')

        # Найти кнопку 'Войти', нажать
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Сравниваем: что название страницы h1 соответствует == 'PetFriends'
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'

        # Поиск элемента-ссылки 'Мои питомцы', и переход по ней
        self.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
        assert self.driver.find_element(By.TAG_NAME, 'h2').text != ''

        # Выясняем количество питонцев и выводим число
        pets_numb = int(
            self.driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(":")[1])
        wait = WebDriverWait(self.driver, 15)
        print('Количество питомцев:', pets_numb)


        # Выясняем имена и породу питомцев, записываем их в массив и выводим на экран
        all_pets = self.driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr')
        pets_data = [pet.text for pet in all_pets]
        not_uniq_pets = set([pet.text for pet in all_pets if pets_data.count(pet.text) > 1])
        pet_names = []
        pet_types = []
        for pet in all_pets:
            pet_names.append(pet.text.split(' ')[0])
            pet_types.append(pet.text.split(' ')[1])
        print('Имена питомцев:', pet_names)
        print('Порода питомцев:', pet_types)
        print(f'Повторящиеся питомцы {not_uniq_pets}')

        
