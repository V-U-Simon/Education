from pprint import pprint
import pymongo
from pymongo import MongoClient
from lesson_02.hh_parse import HeadHunter, Vacancy

client = MongoClient('localhost', 217)
db = client['hh_vacancy']
active = db.active
archive = db.archive


def add_vacancy(vacancy: Vacancy) -> None:
    doc = vacancy._asdict()
    id = doc.pop('position_id')
    active.replace_one({'_id': id}, doc, True)  # add if not exist otherwise update


def filter_gt_salary(salary: int) -> pymongo.cursor.Cursor:
    """ производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы """
    return active.find({'salary': {'$gt': 350000}})


if __name__ == '__main__':
    hh = HeadHunter('python')

    for v in hh.vacancy_list:
        add_vacancy(v)

    for v in filter_gt_salary(300000):
        print('=' * 150)
        pprint(v)
