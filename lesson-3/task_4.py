# Определить, какое число в массиве встречается чаще всего.


m = [6, 4, 8, 4, 5, 2, 7, 2, 3, 4, 3, 9, 6, 0, 4, 5, 1, 1, 6, 8, 1, 8, 7, 1,
     6, 4, 6, 6, 0, 2, 3, 9, 2, 5, 2, 6, 3, 5, 9, 6, 9, 9, 3, 2, 4, 8]
print(m)

result_count = 0
result_nums = 0

for n in set(m):
    count = 0
    for j in m:
        if n == j:
            count += 1
            if count >= result_count:
                result_count = count
                result_nums = j
    print(f'Число {n} повторяется {count} раз')

print(f'Число {result_nums} встречается чаще всего - { result_count} раз.')
