# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import random


def define_characters_position(since: str, until: str) -> str:
    """ Возвращает позиции указанных букв и колличество символов между ними """
    since, until = map(ord, [since, until])
    gap = abs(until - since) - 1 if until != since else 0  # на случай, если совпадают символы
    return since, until, gap


if __name__ == '__main__':
    print(define_characters_position('a', 'b'))
    print(define_characters_position('a', 'c'))
    print(define_characters_position('c', 'a'))
    print(define_characters_position('a', 'a'))
