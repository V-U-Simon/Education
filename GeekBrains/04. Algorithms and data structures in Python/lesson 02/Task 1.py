# Task 1
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа
# Числа и знак операции вводятся пользователем
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя



def calculator():
    """ Обычный калькулятор """

    ACTIONS = {
        "+": lambda digit_1, digit_2: digit_1 + digit_2,
        "-": lambda digit_1, digit_2: digit_1 - digit_2,
        "*": lambda digit_1, digit_2: digit_1 * digit_2,
        "/": lambda digit_1, digit_2: digit_1 / digit_2,
        "0": None
    }

    # VALIDATION
    def check_sigh(sign):
        try:
            ACTIONS[sign]
        except KeyError:
            sign = check_sigh(input("Допустимые значения: '+', '-', '*', '/'б  '0' для вывода: "))
        return sign

    def check_digit(digit):
        try:
            digit = int(digit)
        except ValueError:
            digit = check_digit(input('Повторите ввод, т.к. вы ввели строку вместо числа: '))
        return digit

    sign = check_sigh(input('Введите операцию (+, -, *, / или 0 для вывода): '))
    if sign == "0": return  # BASE CASE
    digit_1 = check_digit(input('Введите число 1: '))
    digit_2 = check_digit(input('Введите число 2: '))

    # MAIN
    print(ACTIONS[sign](digit_1, digit_2))

    # RECURSION FUNCTION
    calculator()


if __name__ == "__main__":
    calculator()
