# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# number_1 = float(input('Первое число: '))
# number_2 = float(input('Второе число: '))
# number_3 = float(input('Третье число: '))

number_1 = 3
number_2 = 9
number_3 = 7

mean = number_1 + number_2 + number_3 - max(number_1, number_2, number_3) - min(number_1, number_2, number_3)

print(f'Число {mean} - среднее')
