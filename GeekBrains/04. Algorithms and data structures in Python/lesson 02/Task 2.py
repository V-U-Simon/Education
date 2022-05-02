# Task 2
# Посчитать четные и нечетные цифры введенного натурального числа
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)


def even_odd_numbers(number, odd=0, even=0):
    """ Возвращает колличество четных и нечетных цифр в числе

    Псевдокод:
    Получает на вход число произвольной длины
    Отделяет последнюю цифру
    вызываем эту-же функцию (таким образом, расчленяем все число)
    - если число не последнее (при целочисленном делении на 10 получается число меньше 1)
    проверяет число на четность
    складывает четные с четными и нечетные с нечетными
    возвращает результат (общее количество четных, нечетных)
    """

    front_ls, last = number // 10, number % 10
    # print(front_ls, last)

    # Базовый случай
    if not last and not front_ls:
        return odd, even

    # Рекурсивный случай
    if last % 2:
        return even_odd_numbers(front_ls, odd + 1, even)
    else:
        return even_odd_numbers(front_ls, odd, even + 1)





if __name__ == '__main__':
    # assert even_odd_numbers(00000) == (5, 0)  # ошибка
    # assert even_odd_numbers(0) == (1, 0)      # ошибка выдает (1, 0)
    assert even_odd_numbers(34560) == (2, 3)
    assert even_odd_numbers(12345) == (3, 2)
    assert even_odd_numbers(2) == (0, 1)
    assert even_odd_numbers(1) == (1, 0)
    # print()
    print(even_odd_numbers(34560))
