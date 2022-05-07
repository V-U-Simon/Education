# Task 6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами
# Сами минимальный и максимальный элементы в сумму не включать

import random

my_max = __import__('Task 4').my_max
my_min = __import__('Task 5').my_min


def get_between(sequence):
    if not sequence: return sequence

    min_el = my_min(sequence)  # Минимальный элемент в последовательности
    min_ind = sequence.index(min_el)  # Первая позиция в массиве минимального элемента

    max_el = my_max(sequence)  # Минимальный элемент в последовательности
    max_ind = sequence.index(max_el)  # Первая позиция в массиве минимального элемента

    return sequence[min_ind + 1:max_ind] if min_ind < max_ind else sequence[max_ind + 1:min_ind]


if __name__ == '__main__':
    assert get_between([3, 10, 4, 9, 8, 8, 3, 0, 3, 5]) == [4, 9, 8, 8, 3]
    assert get_between([3, 0, 4, 9, 8, 8, 3, 10, 3, 5]) == [4, 9, 8, 8, 3]
    assert get_between([]) == []

    # Вывод
    # random_list = [random.randint(-10, 10) for _ in range(10)]  # Исходная последовательность
    random_list = [3, 0, 4, 9, 8, 8, 3, 10, 3, 5]
    print(random_list)
    print(get_between(random_list))
