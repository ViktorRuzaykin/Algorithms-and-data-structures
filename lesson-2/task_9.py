# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

user_data = input('Введите натуральные числа через пробел: ').split(' ')
# user_data = '254 12 54 2547'.split(' ')


def sum_numbers(numbers):
    if len(numbers) == 0:
        return 0
    return int(numbers[0]) + int(sum_numbers(numbers[1:]))


temp_list = [sum_numbers(n) for n in user_data]
temp_dict = {key: value for key, value in zip(temp_list, user_data)}
max_number = max(temp_list)

print(f'Максималная сумма цифр у числа {temp_dict.get(max_number)} равна {max_number}')
