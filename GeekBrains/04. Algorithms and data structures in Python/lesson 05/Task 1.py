# Task 1
# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.
#
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
#
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

from collections import namedtuple
import random
from string import ascii_uppercase
from random import randrange

Company = namedtuple('Company', ('q1', 'q2', 'q3', 'q4'))


def add_companies(*, random_mark=True):
    """ Добавляет компании, в ручном или автоматическом режиме """
    companies = {}
    quantity_of_companies = 4 if random_mark else int(input('Введите количество предприятий: '))

    for _ in range(quantity_of_companies):
        if random_mark:
            name = 'Company ' + ''.join([ascii_uppercase[randrange(len(ascii_uppercase))] for _ in range(3)])
            profit = [random.randint(10, 1000) for _ in range(4)]

        else:
            name = input('Наименование: ')
            profit = []
            for quarter in range(4):
                profit.append(int(input(f'Прибыль за {quarter} квартал: ')))

        companies[name] = Company(*profit)

    return companies


def print_some_average(companies):
    """
    1. show all total average income from all companies
    2. show company if average income higher then from first point
    3. show company if average income lower then from first point
    """

    total_profit = [el
                    for profit in companies.values()
                    for el in profit]

    average_profit = sum(total_profit) / len(companies)
    print(f'Средняя прибыль за год для всех компаний {average_profit}')

    for company, profit in companies.items():
        if sum(profit) > average_profit:
            print(f'Компания c прибылью выше средней {company}')
        else:
            print(f'Компания c прибылью ниже средней {company}')


if __name__ == '__main__':
    companies = add_companies()
    print_some_average(companies)
