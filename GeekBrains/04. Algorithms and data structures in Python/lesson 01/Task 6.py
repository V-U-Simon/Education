# 6. Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.



if __name__ == '__main__':

    number = int(input('input number of character: '))
    print(chr(number) if -1 < number < 1114111 else "There isn't character with this number")
