# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию (индекс) в массиве.


from random import random

m = [int(random() * -100) for i in range(15)]
print(m)

t = -1
for num in m:
    if num < t:
        t = num

print(f'В массиве "m"  максимальный отрицательный элемент: {t}, его индекс: {m.index(t)}')
