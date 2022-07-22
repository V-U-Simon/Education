# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re

from itemadapter import ItemAdapter
from pymongo import MongoClient


class JobparserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vacancy

        # REGULAR EXPRESSION
        self.pattern_id = re.compile(r'\d+')
        self.pattern_tax = re.compile(r'\w+.?$')
        self.pattern_salary = re.compile(r'\d+')
        self.pattern_currency = re.compile(r'USD|руб|EUR')

    def process_item(self, item, spider):
        print()
        item['_id'] = self.process_id(item['_id'], self.pattern_id)
        item['description'] = ''.join(item['description'])
        item['tax_include'] = self.process_tax_include(item['tax_include'])
        item['company'] = ''.join(item['company'])
        item['company_id'] = self.process_id(item['company_id'], self.pattern_id)
        item['company_link'] = 'https://hh.ru' + item['company_link']

        salary_set = ''.join(item['salary']).replace('\u202f', '').replace('\xa0', '')

        item['salary'] = self.process_salary(salary_set, self.pattern_salary)
        item['currency'] = self.process_currency(salary_set, self.pattern_currency) if item['salary'] else None

        collections = self.mongo_base[spider.name]
        collections.replace_one({'_id': item['_id']}, item, True)  # update, if not exist add
        return item

    @staticmethod
    def process_id(id, pattern_id):
        return int(re.search(pattern_id, id)[0])

    @staticmethod
    def process_tax_include(tax: str):
        tax: str
        if tax.endswith('net'):
            return True
        elif tax.endswith('gross'):
            return False
        else:
            return None

    # todo make function convector currency to rubble

    @staticmethod
    def process_currency(salary_set, pattern_currency):
        currency = re.search(pattern_currency, salary_set)[0]
        return currency

    @staticmethod
    def process_salary(salary_set, pattern_salary):

        if salary_set:
            salary = re.findall(pattern_salary, salary_set)

            if len(salary) == 1:
                salary.append(None) if 'от' in salary_set else salary.insert(0, None)  # [100, None] / [None, 100]

                # change type from str ot int
                salary[0] = None if not salary[0] else int(salary[0])
                salary[1] = None if not salary[1] else int(salary[1])

        else:
            salary = [None, None]

        return salary
