# Task 1
# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
#
# Примечание:
# попробуйте написать несколько реализаций алгоритма и сравнить их.
# Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.


# from lesson 3 - task 7
# В одномерном массиве целых чисел определить два наименьших элемента
# Они могут быть как равны между собой (оба являться минимальными), так и различаться

import random
from timeit import timeit


def my_min(sequence, key=lambda x: x):
    """
    Собственная реализация функции min
    key - ключ для возможности использования различных "структур" данных
    """
    # Если один или 0 элементов
    if len(sequence) < 1:
        return sequence

    # Определяем последовательность для перебора
    seq_iter = sequence.__iter__()

    # Определяем первый элемент
    result_el = seq_iter.__next__()
    el_value = key(result_el)

    for el in sequence:

        # Поиск максимума / минимума
        other_el = key(el)
        if other_el < el_value:  # знак максимума / минимума
            el_value = other_el
            result_el = el

    return result_el


def take_two_min_1(seq):
    """
    Сортируем список + выбираем два первых элемента
    (сложность зависит от метода сортировки,
    выбор элементов имеет константную сложность, поэтому отбрасывается
    O(n^2) - в данном примере сложность)
    """
    sorted_list = []
    for i in range(len(seq) - 1):
        min_el = my_min(seq)
        sorted_list.append(min_el)
        seq.remove(min_el)

    return sorted_list[:2]


def take_two_min_2(seq):
    """
    Проходимся по списку, выбирая минимальный
    записываем в res_1 и удаляем этот элемент из основного списка
    снова проходимся по списку в поисках второго минимального элемента
    (сложность в данном случае O(n) поскольку константы отбрасываем,
    O(2n), если точнее - дважды проходим по одному и тому же списку)
    """
    seq = seq.copy()

    first = my_min(seq)
    seq.remove(first)
    second = my_min(seq)
    return first, second


def take_two_min_3(seq):
    """
    Через перебор, но за один проход
    точно есть на яндекс-практикуме (todo: https://www.youtube.com/playlist?list=PL6Wui14DvQPySdPv5NUqV3i8sDbHkCKC5)
    Выбираем за min_1 - первый элемент
    Дальше перебираем оставшуюся часть последовательности
    Если элемент меньше или равен min_1, то записываем в min_2 элемент min_1, а в min_1 записываем текущий элемент
    (сложность в данном случае, o(n), т.к. нет необходимости в двух итерациях)
    """
    if len(seq) <= 1:
        return seq

    min_1, tail = seq[0], seq[1:]
    min_2 = seq[1]

    for el in tail:
        if el <= min_1:
            min_2 = min_1
            min_1 = el
            # continue
        # if el < min_2:
        #     min_2 = el

    return min_1, min_2


def test_time(func, vars):
    for var in vars:
        length = len(var)
        time = timeit('func(var)',
                      number=20,
                      globals={'func': func,
                               'var': var})

        print(f'{func.__name__}{length:.>10}: {time:.6f}')


if __name__ == '__main__':
    # original_random_list = [random.randint(-10, 10) for _ in range(10)]  # Исходная последовательность
    # random_list = original_random_list[:]

    vars = [[random.randint(1, 100) for _ in range(0, 10 ** i)] for i in range(2, 6)]
    test_time(take_two_min_3, vars.copy())
    # take_two_min_3.......100: 0.000039
    # take_two_min_3......1000: 0.000300
    # take_two_min_3.....10000: 0.002967
    # take_two_min_3....100000: 0.029727

    test_time(take_two_min_2, vars.copy())
    #     # take_two_min_2.......100: 0.000188
    #     # take_two_min_2......1000: 0.001773
    #     # take_two_min_2.....10000: 0.016899
    #     # take_two_min_2....100000: 0.173725

    test_time(take_two_min_1, vars.copy())
    #     # take_two_min_1.......100: 0.000271
    #     # take_two_min_1......1000: 0.022833
    #     # take_two_min_1.....10000: 2.246409
