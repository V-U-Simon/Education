# Task 5
# В массиве найти максимальный отрицательный элемент
# Вывести на экран его значение и позицию в массиве

import random


def my_min(sequence, key=lambda x: x):
    """
    Собственная реализация функции min
    key - ключ для возможности использования различных "структур" данных
    """

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


if __name__ == '__main__':
    random_list = [random.randint(-2, 2) for _ in range(10)]  # Исходная последовательность
    min_el = my_min(random_list)  # Минимальный элемент в последовательности
    ind = random_list.index(min_el)  # Первая позиция в массиве минимального элемента

    # Вывод
    print(random_list)
    print('min_el: ', min_el)
    print('index: ', ind)
