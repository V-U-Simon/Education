# Task 2
# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.


first = (8, 3, 15, 6, 4, 2)

# Через генератор
second = [index
          for index, el in enumerate(first)
          if not el % 2]

# Через фукции
even = filter(lambda x: not x % 2, first)
third = list(map(lambda x: first.index(x), even))


if __name__ == '__main__':
    assert second == [0, 3, 4, 5]
    assert third == [0, 3, 4, 5]

    print(second)
    print(third)
