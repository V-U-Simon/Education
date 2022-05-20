# Task 3.
# Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану.
#
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой – не больше медианы.
#
# Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
import random


def selection_sort(data):
    # Внешний цикл (получаем указатель на текущее положение для вставки)
    for i_target in range(len(data) - 1):
        min_idx = i_target  # сначала, считаем за минимальное(максимальное) - текущее значение
        # Внутренний цикл (проходимся в поисках более минимального(максимального), чем min_ind)
        # i_outer_seq - Индекс в диапазоне не отсортированной (левой) части
        # диапазон i_outer_seq при каждой итерации внешнего цикла будет сокращаться
        for i_outer_seq in range(i_target + 1, len(data)):
            if data[i_outer_seq] < data[min_idx]:
                min_idx = i_outer_seq
        data[i_target], data[min_idx] = data[min_idx], data[i_target]
        # наконец меняем самый минимальный(максимальный) элемент с не минимальным(максимальным)
    return data


if __name__ == '__main__':
    length = 5

    seq = [random.randint(-100, 100) for _ in range(2 * length + 1)]
    print(seq)

    selection_sort(seq)
    middle = len(seq) // 2 + 1
    print(seq[middle])
