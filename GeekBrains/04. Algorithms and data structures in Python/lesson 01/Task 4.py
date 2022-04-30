# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
# случайное целое число;
# случайное вещественное число;
# случайный символ.


import random


def random_character(since: str, until: str) -> str:
    """ Возвращает случайны симвом между указанными """
    since, until = map(ord, [since, until])
    return chr(random.randint(since, until))


if __name__ == '__main__':
    print(random.randint(1, 2))
    print(random.uniform(1, 2))
    print(random_character('a', 'z'))
