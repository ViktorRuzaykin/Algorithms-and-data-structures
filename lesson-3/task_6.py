# В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не
# включать.


from random import random

m = [int(random() * 100) for i in range(20)]
print(m)

index_max = m.index(max(m))
index_min = m.index(min(m))

if index_min < index_max:
    new_m = m[index_min + 1:index_max]
else:
    new_m = m[index_max + 1:index_min]

print(new_m)
print(sum(new_m))
