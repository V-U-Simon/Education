# Task 1.
# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.
#
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib


def sub_string_count(text):
    hash_list = []
    text_length = len(text) + 1

    # перебор всех вариантов
    for i in range(text_length):
        for j in range(text_length):

            slice_text = text[i:j]
            hash_str = hashlib.sha1(slice_text.encode('utf-8')).hexdigest()

            if hash_str not in hash_list:
                hash_list.append(hash_str)
                # print(f'{slice_text=}, {hash_str=}')

    count_subs = len(hash_list) - 2  # вычитаем целую строку и пустую подстроку
    return count_subs


if __name__ == '__main__':
    assert sub_string_count('abc') == 5
    print(f"Количество подстрок в abc: {sub_string_count('abc')}")
