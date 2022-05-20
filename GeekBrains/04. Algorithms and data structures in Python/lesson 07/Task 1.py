# Task 1.
# Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).
import random


def buble_from_class(seq: list):
    swapped = False

    # поскольку при каждой итерации мы перегоняем обменом число в конец
    # можем уменьшить количество проходов по последовательности на 1
    for pass_through in range(len(seq) - 1, 0, -1):

        for i in range(pass_through):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True

        if swapped:  # если были перестановки, то еще есть неотсортированные элементы
            swapped = False
        else:  # если пройдясь по всему списку, текущий элемент больше(меньше) следующего
            break  # то можно досрочно прикрывать лавочку, все ок


def buble_sourt(seq: list, reverse=False):
    """
    В сортировке обменами, смысл в обмене местами двух элементов (swap)

    Получаем список на вход
    Идем по списку,
    если следующий элемент меньше текущего, меняем их местами.
    (таким образом подхватываем самый большой элемент и тащим его в конец)

    """

    swapped = True
    if reverse:
        compare = lambda x, y: x < y
    else:
        compare = lambda x, y: x > y

    while swapped:
        swapped = False  # Если пройдясь по списку ни разу не поменяем значения, значит он отсортирован

        for i in range(len(seq) - 1):
            # Пропускаем перестановку, если сортировка двух значений корректна
            if compare(seq[i], seq[i + 1]):
                # if seq[i] < seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True


if __name__ == '__main__':
    seq = [random.randint(-100, 100) for _ in range(10)]
    print(seq)

    # Обе функции возвращают None т.к. имеют side effect (мутируют переданный объект)
    buble_from_class(seq)
    print(seq)
    buble_sourt(seq, reverse=True)
    print(seq)
