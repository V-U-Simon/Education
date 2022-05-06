# Task 1
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9


natural_numbers = range(2, 100)
num_to_check = range(2, 10)

divisible_numbers = {num_check: len([number
                                     for number in natural_numbers
                                     if not number % num_check])

                     for num_check in num_to_check}

print(divisible_numbers)
