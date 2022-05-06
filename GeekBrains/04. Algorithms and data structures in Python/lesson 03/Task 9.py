# Task 9
# Найти максимальный элемент среди минимальных элементов столбцов матрицы


write_matrix = __import__('Task 8').write_matrix
print_matrix = __import__('Task 8').print_matrix
my_min = __import__("Task 5").my_min  # велосипед
my_max = __import__("Task 4").my_max  # велосипед

if __name__ == '__main__':
    matrix = write_matrix(5, 4)
    print_matrix(matrix, end='\n')

    for line in matrix:
        min = my_min(line)
        print(line, ' - ', min)

    max_from_min = my_max([my_min(line) for line in matrix])
    print(max_from_min)
