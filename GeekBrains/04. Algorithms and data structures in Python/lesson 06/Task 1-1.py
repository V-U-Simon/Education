from pympler import asizeof

# Lesson 3 - Task 1
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9
number = 1000
natural_numbers = range(2, number)
num_to_check = range(2, int(number ** 0.5))


# Не оптимизированная версия по памяти
# @profile
def divisible_numbers_by_dict():
    # Пространственная сложность O(n)

    # Line #    Mem usage    Increment  Occurrences   Line Contents
    # =============================================================
    #     14   33.797 MiB   33.797 MiB           1   @profile
    #     15                                         def divisible_numbers_by_dict():
    #     16   33.844 MiB    0.031 MiB       58033       return {num_check: len([number
    #     17   33.844 MiB    0.000 MiB       28971                               for number in natural_numbers
    #     18   33.844 MiB    0.016 MiB       28942                               if not number % num_check])
    #     19
    #     20   33.844 MiB    0.000 MiB          30               for num_check in num_to_check}
    return {num_check: len([number
                            for number in natural_numbers
                            if not number % num_check])

            for num_check in num_to_check}


# Оптимизированная версия по памяти
# @profile
def divisible_numbers_by_gen():
    # Пространственная сложность O(1), но не уверен, т.к. возвращает по одному элементу

    # Line #    Mem usage    Increment  Occurrences   Line Contents
    # =============================================================
    #     26   33.844 MiB   33.844 MiB           1   @profile
    #     27                                         def divisible_numbers_by_gen():
    #     28   33.844 MiB    0.000 MiB           2       return ((num_check, len([number
    #     29                                                                      for number in natural_numbers
    #     30                                                                      if not number % num_check]))
    #     31
    #     32   33.844 MiB    0.000 MiB           1               for num_check in num_to_check)
    return ((num_check, len([number
                             for number in natural_numbers
                             if not number % num_check]))

            for num_check in num_to_check)


if __name__ == '__main__':
    print(asizeof.asizeof(divisible_numbers_by_dict()))  # size 3032
    print(asizeof.asizeof(divisible_numbers_by_gen()))  # size 440 (все генераторы весят 440)
