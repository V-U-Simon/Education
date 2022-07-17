from collections import namedtuple

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pymongo import MongoClient

# MONGO_DB
client = MongoClient('localhost', 217)  # указываем ip/port
db = client['mailru']  # БД
inbox = db.inbox  # Коллекция

# DATA_FORMAT
Letter = namedtuple('Letter', 'id, url, mail_from, mail_to, mail_date, mail_subject, mail_body')

# BROWSER
options = Options()
# options.add_argument("--headless")  # ❌ 📺 запуск без графического интерфейса
# options.add_argument('start-maximized')  # размер экрана
service = Service('./chromedriver')  # путь до драйвера


def get_all_mail(login: str, password: str):
    """ Save all letters into DB_mongo """
    with webdriver.Chrome(service=service, options=options) as driver:
        driver.get('https://account.mail.ru/')
        driver.implicitly_wait(5)

        # LOGIN
        login_page = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
        login_page.send_keys(login)

        button_login = driver.find_element(By.CSS_SELECTOR, "button[data-test-id='next-button']")
        button_login.click()

        password_page = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_page.send_keys(password)
        password_page.submit()

        # OPEN MAIL
        mail = driver.find_element(By.CSS_SELECTOR, "div[role='rowgroup'] > a ")
        mail.click()

        def switch_to_next_page():
            try:
                # Если кнопка переключения серая, то письма закончились
                next_page = driver.find_element(By.CSS_SELECTOR,
                                                ".portal-menu__group div:last-child > span:not(.button2_disabled)")
                next_page.click()
                return True
            except NoSuchElementException:
                print('this was the last page')
                return False

        while True:
            # driver.implicitly_wait(5)
            time.sleep(2)
            # СБОР ДАННЫХ (от кого, дата отправки, тема письма, текст письма полный)
            url = driver.current_url  # 'https://e.mail.ru/inbox/0:16582205691033180354:0/?afterReload=1'
            print(url)
            _id = str(url).split(':')[2]  # ['https', '//e.mail.ru/inbox/0', '16582205691033180354', '0/?afterReload=1']
            mail_from = driver.find_element(By.CSS_SELECTOR, ".letter__author .letter-contact").get_attribute('title')
            mail_to = driver.find_element(By.CSS_SELECTOR, ".letter__recipients .letter-contact").get_attribute('title')
            mail_date = driver.find_element(By.CSS_SELECTOR, ".letter__author .letter__date").text
            mail_subject = driver.find_element(By.CSS_SELECTOR, "h2.thread-subject").text
            # mail_body_html = driver.find_element(By.CSS_SELECTOR, "div.letter-body tbody")
            mail_body = driver.find_element(By.CSS_SELECTOR, ".letter-body").text

            letter = Letter(_id, url, mail_from, mail_to, mail_date, mail_subject, mail_body)
            letter = letter._asdict()

            # ЗАПИСЬ ДАННЫХ
            inbox.replace_one({'_id': letter.pop('id')}, letter, True)

            if not switch_to_next_page():
                # Если не переключились на следующую страницу, то выходим из цикла
                break


if __name__ == '__main__':
    # TODO: use environment variable
    login = ''
    password = ''

    get_all_mail(login, password)
