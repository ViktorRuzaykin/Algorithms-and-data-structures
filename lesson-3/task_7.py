# В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть
# как равны между собой (оба являться минимальными), так и различаться.


from random import random

m = [int(random() * 100) for i in range(10)]
print(m)

"""min_nums_list = [min(m)]
tmp_list = m[:]
tmp_list.remove(min_nums_list[0])
min_nums_list.append(min(tmp_list))

print(min_nums_list)
print(m)"""

min_num_1 = m[0]
min_num_2 = m[0]

for n in m:
    if n < min_num_1:
        min_num_1 = n

if m.count(min_num_1) == 1:
    for j in m:
        if j < min_num_2 and j != min_num_1:
            min_num_2 = j
else:
    min_num_2 = min_num_1

print(f'min_num_1: {min_num_1}, min_num_2: {min_num_2}')
