from memory_profiler import profile
from pympler import asizeof


# Lesson 3 - Task 2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


# Через генератор
@profile()
def even_1():
    # Пространственная сложность O(n), сразу генерируется лист со значениями

    # Line #    Mem usage    Increment  Occurrences   Line Contents
    # =============================================================
    #     17     58.4 MiB     58.4 MiB           1   @profile()
    #     18                                         def even_1():
    #     19     58.7 MiB      0.4 MiB      200002       return [index
    #     20     58.7 MiB      0.0 MiB      100000               for index, el in enumerate(source)
    #     21     58.7 MiB      0.0 MiB       99999               if not el % 2]

    return [index
            for index, el in enumerate(source)
            if not el % 2]


# Через фукции
@profile()
def even_2():
    # Пространственная сложность O(n), дополнительно генерируется временная

    # Line #    Mem usage    Increment  Occurrences   Line Contents
    # =============================================================
    #     25     64.0 MiB     64.0 MiB           1   @profile()
    #     26                                         def even_2():
    #     27     64.0 MiB      0.0 MiB      199999       tmp = filter(lambda x: not x % 2, source)
    #     28     64.0 MiB      0.0 MiB       99999       return list(map(lambda x: source.index(x), tmp))

    tmp = filter(lambda x: not x % 2, source)
    return list(map(lambda x: source.index(x), tmp))


if __name__ == '__main__':
    source = [_ for _ in range(1, 100000)]
    print(asizeof.asized(source))  # size 4000952, flat 800984, refs[0]
    print(asizeof.asized(even_1()))  # size 2044344, flat 444376, refs[0]
    print(asizeof.asized(even_2()))  # size 2044344, flat 444376, refs[0]
