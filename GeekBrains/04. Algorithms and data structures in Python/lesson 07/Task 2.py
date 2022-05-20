# Task 2.
# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_two_list(first, second):
    """ Принимает на вход отсортированные списки """

    res_list = []
    i = j = 0
    # Пока индекс не дошел до предела списка одного из списков
    while i < len(first) and j < len(second):
        # Сравниваем элементы и добавляем меньший(больший) в результирующий список
        if first[i] < second[j]:
            res_list.append(first[i])
            i += 1
        else:
            res_list.append(second[j])
            j += 1

    # Длина суммы список не четная
    # Если один из списков закончился (но мы не знаем который)
    if i < len(first):
        res_list += first[i:]
    if j < len(second):
        res_list += second[j:]
    return res_list


def merge_sort(seq):
    # Функция вызывается до тех пор, пока не разделит последовательность до одного элемента
    # Затем поочередно соединяет их попутно сортируя
    if len(seq) == 1:  # Базовый случай
        return seq

    middle_of_seq = len(seq) // 2
    left = merge_sort(seq[:middle_of_seq])  # Рекурсивный случай
    right = merge_sort(seq[middle_of_seq:])  # Рекурсивный случай

    return merge_two_list(left, right)


if __name__ == '__main__':
    seq = [random.randint(0, 50) for _ in range(10)]
    print(seq)
    print(merge_sort(seq))
