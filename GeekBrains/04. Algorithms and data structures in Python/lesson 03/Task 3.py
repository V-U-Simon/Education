# Task 3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
import random


def my_reverse(sequence):
    """ Вывод последовательностей в обратном поярдке """
    sequence = sequence.copy()
    iterations = range(len(sequence) // 2)

    for i in iterations:
        sequence[-i - 1], sequence[i] = sequence[i], sequence[-i - 1]

    return sequence


if __name__ == '__main__':
    # random_list = [random.randint(1, 10) for _ in range(6)]
    random_list = [10, 2, 3, 9, 0, 2, 1]

    assert list(reversed(random_list[:])) == [1, 2, 0, 9, 3, 2, 10]
    assert my_reverse(random_list[:]) == [1, 2, 0, 9, 3, 2, 10]
