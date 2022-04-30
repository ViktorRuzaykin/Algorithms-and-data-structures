# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


user_data = '34560'
# user_data = input('Введите натуральное число: ')

even_list = []
not_even_list = []
even = 0
not_even = 0

for n in user_data:
    if int(n) % 2 == 0:
        even += 1
        even_list.append(n)
    else:
        not_even += 1
        not_even_list.append(n)

print(f'В введенном числе "{user_data}" '
      f'{even} четные числа {tuple(even_list)} и {not_even} нечетные {tuple(not_even_list)}')
