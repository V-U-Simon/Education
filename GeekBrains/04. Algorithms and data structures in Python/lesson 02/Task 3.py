# Task 3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран
# Например, если введено число 3486, то надо вывести число 6843


def decorator(func):
    """ Декоратор для приведения результата цункции к int """

    def inside_function(*args, **kwargs):
        res = func(*args, **kwargs)
        return int(res)

    return inside_function


@decorator
def opposite_direction_numbers(number: int) -> str:
    """ Возвращает в числа в обратном порядке """

    front, tail = number // 10, number % 10

    return tail if not front else str(tail) + str(opposite_direction_numbers(front))
    #           ^ BASE CASE                       ^ RECURSIVE FUNCTION


if __name__ == '__main__':
    assert opposite_direction_numbers(123) == 321
    assert opposite_direction_numbers(1230) == 321
    assert opposite_direction_numbers(0) == 0
