# Task 2
# Написать два алгоритма нахождения i-го по счёту простого числа.
#
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
#
# Примечание:
# # Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

# n = int(input("вывод простых чисел до числа ... "))
import math
from itertools import count
from timeit import timeit


def explanation_sieve_of_eratosthenes(n):
    """
    Как работает решето Эратосфена?

    1. Все четные числа, кроме двойки, - составные, т. е. не являются простыми,
    так как делятся не только на себя и единицу, а также еще на 2.

    2. Все числа кратные трем, кроме самой тройки, - составные,
    так как делятся не только на самих себя и единицу, а также еще на 3.

    3. Число 4 уже выбыло из игры, так как делится на 2.

    4. Число 5 простое, так как его не делит ни один простой делитель, стоящий до него.

    5. Если число не делится ни на одно простое число, стоящее до него,
    значит оно не будет делиться ни на одно сложное число, стоящее до него.
    """

    # список значений
    array = [_ for _ in range(n + 1)]

    # Вторым элементом является единица,
    # которую не считают простым числом
    # забиваем ее нулем.
    array[1] = 0

    # начинаем с 3-го элемента
    i = 2  # [0, 0, 2, ... ] двойка третья по индексу
    while i <= n:  # до тех пор, пока индекс меньше или равен пределу проверяемых чисел:

        # Если значение ячейки - простое число, наименьшее,
        # То удаляем все числа, которые могут из него состоять (заменено на ноль, альтернатива удаления),
        if array[i] != 0:

            # Тут удаляем все кратные числу i, т.е. составные
            j = i + i  # <- перебираем все составные числа

            while j <= n:  # до тех пор пока составное число меньше или равно предельному числу...
                array[j] = 0  # ...  удаляем его

                j = j + i  # прибавляем i (к удаленному числу) для получения очередного состовного числа
                # после, идем на следующий заход

        i += 1  # смотрим следующее число в нашем массиве

    # избавляемся от всех нулей кроме одного.
    array = [el for el in array if el]
    return array


def sieve_of_eratosthenes_throw_set(n):
    """ Вариант реализации через множества """
    all = frozenset(_ for _ in range(2, n))
    edge = int(n ** 0.5)

    for i in range(2, edge + 1):
        all = all - {_ for _ in range(i + i, 100, i)}

    return list(all)


def find_prime(n):
    """
    Поиск i-го простого числа без использования алгоритма «Решето Эратосфена»

    1. Берем число из последовательности
    2. Если это число не составное (не делится ни на одно из находящихся в списке простых),
    3. то добавляем его к простым
    4. Когда длина списка, сравнивается с заданным пользователем числом - останавливаемся


    """

    numbers = count(3, 2).__iter__()  # аналог - for number in numbers, шаг 2, т.к. 2 уже в простых числах
    prime_list = [2, ]  # делители / простые числа

    while len(prime_list) < n:
        number = numbers.__next__()

        for divider in prime_list:  # пробегаем все числа от 2 до текущего в поисках делителя
            if number % divider == 0:  # если делитель найден, число не простое.
                break
        else:  # Выполняем, если отрабатывает brake
            prime_list.append(number)  # добавляем число в список

    return prime_list[-1]


def sieve(n):
    '''
    Поиск i-го простого числа с использованием алгоритма «Решето Эратосфена»
    '''

    def sieve_it(n):
        primes = [i for i in range(n)]
        primes[1] = 0

        for i in range(2, n):
            if primes[i] != 0:
                j = i + i
                while j < n:
                    primes[j] = 0
                    j += i
        return primes

    lim = n
    primes_found = 0
    while primes_found < n:
        lst = sieve_it(lim)
        for num in lst:
            if num != 0:
                primes_found += 1
            if primes_found == n:
                return num
        lim *= 2
        primes_found = 0


def sieve_2(i):
    '''
    Поиск i-го простого числа с использованием алгоритма «Решето Эратосфена»
    '''

    def prime_counting_function(i):
        number_of_primes = 0
        number = 2
        while number_of_primes <= i:
            number_of_primes = number / math.log(number)
            number += 1
        return number

    # todo: разобрать позднее, sieve_2(2) - IndexError: list index out of range
    if i == 2:
        return 2

    end = prime_counting_function(i)

    primes = [_ for _ in range(2, end)]

    for number in primes:
        if primes.index(number) <= number - 1:
            for j in range(2, len(primes)):
                if number * j in primes[number:]:
                    primes.remove(number * j)  # удаляем лишние числа
        else:
            break
    return primes[i - 1]


def test_time(func):
    vars = [2 ** i for i in range(1, 15)]

    for var in vars:
        time = timeit('func(var)',
                      number=20,
                      globals={'func': func,
                               'var': var})

        print(f'{func.__name__}{var:.>10}: {time:.6f}')


if __name__ == '__main__':
    test_time(find_prime)
    # find_prime.........2: 0.000016
    # find_prime.........4: 0.000024
    # find_prime.........8: 0.000065
    # find_prime........16: 0.000206
    # find_prime........32: 0.000661
    # find_prime........64: 0.002206
    # find_prime.......128: 0.007001
    # find_prime.......256: 0.023790
    # find_prime.......512: 0.067104
    # find_prime......1024: 0.262055
    # find_prime......2048: 1.065585

    test_time(sieve)
    # sieve.........2: 0.000041
    # sieve.........4: 0.000061
    # sieve.........8: 0.000232
    # sieve........16: 0.000464
    # sieve........32: 0.002009
    # sieve........64: 0.003939
    # sieve.......128: 0.007758
    # sieve.......256: 0.014779
    # sieve.......512: 0.025229
    # sieve......1024: 0.047116
    # sieve......2048: 0.193199

    test_time(sieve_2)
    # sieve_2.........2: 0.000001
    # sieve_2.........4: 0.000076
    # sieve_2.........8: 0.000256
    # sieve_2........16: 0.001212
    # sieve_2........32: 0.006036
    # sieve_2........64: 0.030847
    # sieve_2.......128: 0.166641
    # sieve_2.......256: 0.913115
    # sieve_2.......512: 5.477449
    # sieve_2......1024: 34.014938
    # sieve_2......2048: 222.890218
    # todo: решето должно работать быстрее
