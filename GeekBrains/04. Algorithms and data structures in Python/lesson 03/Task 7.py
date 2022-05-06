# Task 7
# В одномерном массиве целых чисел определить два наименьших элемента
# Они могут быть как равны между собой (оба являться минимальными), так и различаться


import random

# Импорт функции из файла в имени которого есть пробел
my_min = __import__("Task 5").my_min

if __name__ == '__main__':
    original_random_list = [random.randint(-10, 10) for _ in range(10)]  # Исходная последовательность
    random_list = original_random_list[:]

    first_min_el = my_min(random_list)  # Минимальный элемент в последовательности
    ind = random_list.index(first_min_el)  # Первая позиция в массиве минимального элемента
    del random_list[ind]
    second_min_el = my_min(random_list)  # Минимальный элемент в последовательности

    assert sorted(original_random_list)[1] == second_min_el

    print(sorted(original_random_list))
    print(second_min_el)
