# Task 2
# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как ['A', '2'] и ['C', '4', 'F'] соответственно.
# Сумма чисел из примера: ['C', 'F', '1'], произведение - ['7', 'C', '9', 'F', 'E'].
#
# Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections


from collections import deque

# Таблица шестнадцатеричных чисел
HEX = list(map(str,
               (range(0, 10)))) + ['A', 'B', 'C', 'D', 'E', 'F', '10']


def sixteen_to_ten(number):
    """ Перевод из шестнадцатеричной в десятичную """
    number.reverse()
    return sum((HEX.index(num) * 16 ** i)
               for i, num in enumerate(number))


def ten_to_sixteen(number):
    """ Перевод из десятичной в шестнадцатеричную """
    res = deque()
    while number > 16:
        res.append(HEX[number % 16])
        number = number // 16
    res.append(HEX[number % 16])
    res.reverse()
    return res


if __name__ == '__main__':
    print(ten_to_sixteen(sixteen_to_ten(['A', '2']) + sixteen_to_ten(['C', '4', 'F'])))
    print(ten_to_sixteen(sixteen_to_ten(['A', '2']) * sixteen_to_ten(['C', '4', 'F'])))
