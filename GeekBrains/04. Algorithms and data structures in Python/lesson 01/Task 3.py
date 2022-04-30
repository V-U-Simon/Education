# По введенным пользователем координатам двух точек вывести уравнение прямой
# вида y = kx + b, проходящей через эти точки


def linear_equation(x1: int, y1: int, x2: int, y2: int) -> str:
    if x1 == x2 == y1 == y2:
        # raise Exception(ValueError, 'Обе точки находятся в одном месте')
        return False
    elif x1 - x2 == 0:
        print(f'точки А и В лежат на прямой ')
        return f'y = {x1}'
    elif y1 - y2 == 0:
        print(f'точки А и В лежат на прямой ')
        return f'x = {y1}'
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y1 - (y2 - y1) / (x2 - x1)

        if b > 0:
            return f'y = {k}x + {b}'
        elif b < 0:
            # если график ниже 0 убираем минус для красивого отображения
            return f'y = {k}x - {abs(b)}'
        else:
            return f'y = {k}x'


if __name__ == '__main__':
    assert linear_equation(1, 1, 1, 1) == False
    assert linear_equation(1, 3, 1, 2) == 'y = 1'
    assert linear_equation(1, 2, 5, 2) == 'x = 2'
    assert linear_equation(1, 1, 5, 2) == 'y = 0.25x + 0.75'
    assert linear_equation(-12, -3, -2, -6) == 'y = -0.3x - 2.7'

    x1, y1 = map(int, input("Введите координаты первой точки 1 через ',': ").split(','))
    x2, y2 = map(int, input("Введите координаты второй точки 2 через ',': ").split(','))
