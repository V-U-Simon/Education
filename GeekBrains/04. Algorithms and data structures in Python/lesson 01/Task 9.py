# 9. Вводятся три разных числа.
# Найти, какое из них является средним (больше одного, но меньше другого).

def middle(a, b, c):
    sorted_list = sorted((a, b, c))
    return sorted_list[1]


if __name__ == '__main__':
    print(middle(1, 2, 3))
    print(middle(2, 2, 3))
    print(middle(3, 2, 2))
    print(middle(0, 0, 0))
