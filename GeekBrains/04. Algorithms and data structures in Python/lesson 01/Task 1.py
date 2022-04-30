"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


def find_sum_and_pr(numbers: int) -> tuple[int, int]:
    """сумма и произведение трех цифр"""

    a = numbers // 100
    b = numbers // 10 % 10
    c = numbers % 10

    sum_numbers = a + b + c
    pr_numbers = a * b * c

    return pr_numbers, sum_numbers


if __name__ == '__main__':
    numbers = int(input('Введите трехзначное число: '))
    print('Прозведение: {0[0]}, Сумма {0[1]}'.format(find_sum_and_pr(numbers)))  # (24, 9)
