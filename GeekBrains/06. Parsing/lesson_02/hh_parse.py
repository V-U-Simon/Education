from __future__ import annotations
import re
from time import sleep
from random import randint
import traceback
from typing import NamedTuple
from datetime import datetime
import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from collections import namedtuple

# from pprint import pprint


Vacancy = namedtuple('Vacancy',
                     'position_id, position, position_link, company, company_link, location, salary, currency, date')


class HeadHunter:

    def __init__(self, http_params):
        # SELECTORS
        # super().__init__()
        self._selector_end_pages = '.pager a:last-child'
        self._selector_content_list = '[id$=main-content] [class$=item-body]'
        self._selector_position = 'a[data-qa*=title]'
        self._selector_position_link = 'a[data-qa*=title]'
        self._selector_company = '[class$=info-company]'
        self._selector_company_link = '[class$=info-company] a'
        self._selector_location = '[data-qa$=serp__vacancy-address]'
        self._selector_salary_set = ':first-child span[data-qa]'

        # HTTP
        self._http_headers = {'User-Agent': UserAgent().chrome}
        self._search_position = http_params
        self._url = 'https://hh.ru/search/vacancy/'
        self._page = 0

        # HTML
        self.vacancies = None
        self._html_dom = None
        self._html = None

        # Session
        self.http_session = requests.session()

    # MAIN
    @property
    def vacancy_list(self):
        while True:
            # http request
            sleep(randint(1, 3))
            self._page += 1
            response = self.request_get(self._page)
            if not response.ok:
                # todo: print to log
                continue

            # progress bar
            print(self._page)

            # parse
            self._html = response.text
            self._html_dom = BeautifulSoup(self._html, features='lxml')
            self.vacancies = self.get_parsed_data(self._html_dom)

            for vacancy in self.vacancies:
                yield vacancy
                # self.safe(v, 'vacancy.json')

            if not self.is_last_page:
                break

    # HTTP
    def request_get(self, page: int) -> requests.Response:
        return self.http_session.get(self._url,
                                     headers=self._http_headers,
                                     params={'page': page,
                                             'text': self._search_position,  # search query
                                             'items_on_page': 20})

    # PARSE
    @property
    def is_last_page(self) -> bool:
        if self._html_dom.select_one(self._selector_end_pages):
            return True
        return False

    @staticmethod
    def _parse_salary(salary_set, pattern_currency, pattern_salary):
        if salary_set:
            salary_set = salary_set.text.replace('\u202f', '')  # todo: посмотреть как сделал при кодировке

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

    @staticmethod
    def _parse_id(href, pattern_id):
        # REGULAR EXPRESSION
        if href:
            return int(re.search(pattern_id, href)[0])

    def get_parsed_data(self, html_dom) -> Vacancy:
        content_list = html_dom.select(self._selector_content_list)

        # REGULAR EXPRESSION
        pattern_currency = re.compile(r'\w+.?$')
        pattern_id = pattern_salary = re.compile(r'\d+')

        for content in content_list:
            try:
                position = content.select_one(self._selector_position).text
                position_link = content.select_one(self._selector_position_link).get('href')
                position_id = self._parse_id(position_link, pattern_id)
                company = content.select_one(self._selector_company).get_text(separator=' ', strip=True)
                company_link = 'https://hh.ru' + content.select_one(self._selector_company_link).get('href')
                location = content.select_one(self._selector_location).get_text(separator=' ', strip=True)
                salary_set = content.select_one(self._selector_salary_set)
                salary, currency = self._parse_salary(salary_set, pattern_currency, pattern_salary)
                date = datetime.utcnow()

                yield Vacancy(position_id, position, position_link,
                              company, company_link, location,
                              salary, currency, date)

            except Exception as e:
                print(f'parse error on {self._url}: {e}')
                print("traceback.print_exc():")
                traceback.print_exc()
                print("____")


# JSON Save
def json_safe(file_name, data):
    encoding = "utf-8"
    with open(file_name, 'a+', encoding=encoding) as f:
        to_save = json.dumps(data)
        f.write(to_save + '\n')
    return True


if __name__ == '__main__':
    hh = HeadHunter('python')

    for vacancy in hh.vacancy_list:
        print(vacancy)
        json_safe('vacancy.json', vacancy)
