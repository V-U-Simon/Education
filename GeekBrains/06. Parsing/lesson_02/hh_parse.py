import re
from pprint import pprint
from time import sleep
from random import randint
import traceback

import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from collections import namedtuple

Vacancy = namedtuple('Vacancy', 'position, position_link, company, company_link, location, salary, currency')


class HH_Selectors:
    def __init__(self):
        self._selector_end_pages = '.pager a:last-child'

        self._selector_content_list = '[id$=main-content] [class$=item-body]'
        self._selector_position = 'a[data-qa*=title]'
        self._selector_position_link = 'a[data-qa*=title]'
        self._selector_company = '[class$=info-company]'
        self._selector_company_link = '[class$=info-company] a'
        self._selector_location = '[data-qa$=serp__vacancy-address]'
        self._selector_salary_set = ':first-child span[data-qa]'


class HeadHunter(HH_Selectors):

    def __init__(self, search_position):
        # SELECTORS
        super().__init__()

        # MAIN FLOW
        self.url = 'https://hh.ru/search/vacancy/'
        self.last_page = False
        self.http_header = {'User-Agent': UserAgent().chrome}
        self.http_params = {'page': 1,
                            'text': search_position,  # search query
                            'items_on_page': 20}

        self.http_session = requests.session()

        while not self.last_page:
            # http request
            print(self.http_params['page'])  # progress bar
            self.html = self.html_request()
            self.http_params['page'] += 1
            sleep(randint(1, 3))

            # parse
            self.parse_content()
            self.vacancy = self.parse_content_vacancy()
            for v in self.vacancy:
                self.safe(v, 'vacancy.json')
            # if self.last_page:
            #     self.last_page = True

    def html_request(self):
        # url, search, http_header, http_params={}
        """ Make request, get html """
        response = self.http_session.get(self.url,
                                         headers=self.http_header,
                                         params=self.http_params)
        self.html_url = response.url
        # print(f'http request by url: {self.html_url}')
        return response.text

    def parse_content(self):
        self.html_dom = BeautifulSoup(self.html, features='lxml')
        self.content_list = self.html_dom.select(self._selector_content_list)
        # проверяет наличие ссылки на последнюю страницу (по умолчанию False)
        self.last_page = not bool(self.html_dom.select_one(self._selector_end_pages))

    def parse_content_vacancy(self):
        """ get content from DOM """
        # SELECTORS
        for content in self.content_list:
            try:
                position = content.select_one(self._selector_position).text
                position_link = content.select_one(self._selector_position_link).get('href')
                company = content.select_one(self._selector_company).get_text(separator=' ', strip=True)
                company_link = 'https://hh.ru' + content.select_one(self._selector_company_link).get('href')
                location = content.select_one(self._selector_location).get_text(separator=' ', strip=True)
                salary_set = content.select_one(self._selector_salary_set)

                salary, currency = HeadHunter.__parse_salary(salary_set)

                yield Vacancy(position, position_link, company, company_link, location, salary, currency)
            except Exception as e:
                print(f'parse error on {self.html_url}: {e}')
                print("traceback.print_exc():")
                traceback.print_exc()
                print("____")

    @staticmethod
    def __parse_salary(salary_set):
        """ parse salary data """
        # REGULAR EXPRESSION
        pattern_currency = re.compile(r'\w+.?$')
        pattern_salary = re.compile(r'\d+')

        if salary_set:
            salary_set = salary_set.text.replace('\u202f', '')

            currency = re.search(pattern_currency, salary_set)[0]
            salary = re.findall(pattern_salary, salary_set)

            if len(salary) == 1:
                salary.append(None) if 'от' in salary_set else salary.insert(0, None)
        else:
            salary = [None, None]
            currency = None

        # change type from str ot int
        salary[0] = None if not salary[0] else int(salary[0])
        salary[1] = None if not salary[1] else int(salary[1])

        # todo make function convector currency to rubble
        # currency = None if not currency else currency.replace('.', '')
        return salary, currency

    # JSON Save
    def safe(self, data, file_name):
        """ сохряняем в json """
        encoding = "utf-8"
        with open(file_name, 'a+', encoding=encoding) as f:
            to_save = json.dumps(data)
            f.write(to_save + '\n')
        return True

    def load(self, file_name):
        """ загружаем из json """
        encoding = "utf-8"

        with open(file_name, 'r', encoding=encoding) as f:
            return [json.loads(line) for line in f]


if __name__ == '__main__':
    hh = HeadHunter('python')
