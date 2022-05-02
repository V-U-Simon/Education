# Task 4
# Найти сумму n элементов следующего ряда чисел:
# 1 -0.5 0.25 -0.125...
# Количество элементов (n) вводится с клавиатуры.


def rec_sum(iteration, start_number=1):
    """
    Псевдокод

    Вводим индекс с количеством итераций - i
    first = 1 | Начинаем с единицы
    уменьшаем количество итераций i -= 1

    Рекурсивный случай
    Если i >= 1
        складываем first + c вызыванной функцией(передаем номер итерации - i,
                                               передаем текущее (обработанное) состояние первого числа)
                                               Так на каждой итерации мы делим first на -2
    Базовый случай
    Если i == 0 -> возвращаем результат последней итерации
    """

    iteration -= 1

    # Рекурсивный случай
    if iteration >= 1:
        return start_number + rec_sum(iteration, start_number / -2)

    # Базовый случай
    return start_number

if __name__ == '__main__':
    assert rec_sum(iteration=4) == 0.625
    assert rec_sum(iteration=0) == 1
    assert rec_sum(iteration=-1) == 1
    assert rec_sum(iteration=2) == 0.5

    print(rec_sum(iteration=4))
