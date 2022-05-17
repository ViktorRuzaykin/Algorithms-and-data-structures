# В массиве случайных целых чисел поменять местами минимальный и максимальный
# элементы.


from random import random

m = [int(random() * 100) for i in range(20)]
print(m)

max_num = m[0]
min_num = m[0]

for number in m:
    if max_num < number:
        max_num = number
    if min_num > number:
        min_num = number

print(f'Минимальный элемент: {min_num}, максимальный элемент: {max_num}')

m[m.index(max_num)] = min_num
m[m.index(min_num)] = max_num
print(m)
