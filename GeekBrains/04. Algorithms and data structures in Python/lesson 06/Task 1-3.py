from memory_profiler import profile
import random
from collections import Counter, defaultdict
from pympler import asizeof


# Lesson 3 - Task 4
# Определить, какое число в массиве встречается чаще всего

def my_max(sequence, key=lambda x: x):
    """
    Собственная реализация функции min
    key - ключ для возможности использования различных "структур" данных
    """

    # Определяем последовательность для перебора
    seq_iter = sequence.__iter__()

    # Определяем первый элемент
    result_el = seq_iter.__next__()
    el_value = key(result_el)

    for el in seq_iter:

        # Поиск максимума / минимума
        other_el = key(el)
        if other_el > el_value:  # знак максимума / минимума
            el_value = other_el
            result_el = el

    return result_el


# Функциональщина
@profile()
def throw_fucn():
    # Line #    Mem usage    Increment  Occurrences   Line Contents
    # =============================================================
    #     36     42.8 MiB     42.8 MiB           1   @profile()
    #     37                                         def throw_fucn():
    #     38     42.8 MiB      0.0 MiB           1       elements_1 = Counter(random_list)
    #     39     42.8 MiB      0.0 MiB          13       return max(elements_1, key=lambda el: elements_1[el])

    elements_1 = Counter(random_list)
    return max(elements_1, key=lambda el: elements_1[el])


# Генератор
@profile()
def throw_comprehension():
    # Line #    Mem usage    Increment  Occurrences   Line Contents
    # =============================================================
    #     43     42.8 MiB     42.8 MiB           1   @profile()
    #     44                                         def throw_comprehension():
    #     45     42.8 MiB      0.0 MiB          13       elements_2 = {el: random_list.count(el) for el in random_list}
    #     46     42.8 MiB      0.0 MiB          13       return max(elements_2, key=lambda el: elements_2[el])

    elements_2 = {el: random_list.count(el) for el in random_list}
    return max(elements_2, key=lambda el: elements_2[el])


# Цикл
@profile()
def throw_cycle():
    # Line #    Mem usage    Increment  Occurrences   Line Contents
    # =============================================================
    #     50     42.8 MiB     42.8 MiB           1   @profile()
    #     51                                         def throw_cycle():
    #     52     42.8 MiB      0.0 MiB           1       elements_3 = defaultdict(int)
    #     53     42.8 MiB      0.0 MiB          11       for el in random_list:
    #     54     42.8 MiB      0.0 MiB          10           elements_3[el] += 1
    #     55
    #     56     42.8 MiB      0.0 MiB          13       return my_max(elements_3, key=lambda el: elements_3[el])

    elements_3 = defaultdict(int)
    for el in random_list:
        elements_3[el] += 1

    return my_max(elements_3, key=lambda el: elements_3[el])


if __name__ == '__main__':
    # Исходная последовательность
    random_list = [chr(random.randint(97, 102)) for _ in range(10)]  # size 520, flat 184, refs[0]

    print(asizeof.asized(throw_fucn()))  # size 56, flat 56, refs[0], name "'d'"
    print(asizeof.asized(throw_comprehension()))  # size 56, flat 56, refs[0], name "'d'"
    print(asizeof.asized(throw_cycle()))  # size 56, flat 56, refs[0], name "'d'"
