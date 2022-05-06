# Task 4
# Определить, какое число в массиве встречается чаще всего
import random
from collections import Counter, defaultdict


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


if __name__ == '__main__':
    # Исходная последовательность
    random_list = [chr(random.randint(97, 102)) for _ in range(10)]

    # Функциональщина
    elements_1 = Counter(random_list)
    max_elem_1 = max(elements_1, key=lambda el: elements_1[el])

    # Генератор
    elements_2 = {el: random_list.count(el) for el in random_list}
    max_elem_2 = max(elements_2, key=lambda el: elements_2[el])

    # Цикл
    elements_3 = defaultdict(int)
    for el in random_list:
        elements_3[el] += 1

    max_elem_3 = my_max(elements_3, key=lambda el: elements_3[el])
    # max_elem_3 = max(elements_3, key=lambda el: elements_3[el])

    # Вывод
    print(random_list)
    print(max_elem_1)
    print(max_elem_2)
    print(max_elem_3)
