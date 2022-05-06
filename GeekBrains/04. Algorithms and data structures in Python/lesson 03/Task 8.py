# Task 8
# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки
# В конце следует вывести полученную матрицу
import random


def write_matrix(lines: 1, columns: 1, random_data=True):
    """ Заполнение матрицы """
    data = lambda: random.randint(1, 9) if random_data else int(input('Write number: '))

    # lines
    def write_lines():
        return [data() for _ in range(lines)]

    # column
    return [write_lines() for _ in range(columns)]


def print_matrix(matrix, end=None):
    """ Печатает матрицу """
    for line in matrix:
        print(line)

    if end: print(end)


def count_number_in_line(matrix):
    """ Считает сумму строки и добавдят ее в конец """
    for line in matrix:
        line: list
        line.append(sum(line))


if __name__ == '__main__':
    matrix = write_matrix(5, 4)
    print_matrix(matrix)
    count_number_in_line(matrix)
    print_matrix(matrix)
