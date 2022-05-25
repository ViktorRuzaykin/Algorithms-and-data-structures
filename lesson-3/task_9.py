# Найти максимальный элемент среди минимальных элементов столбцов матрицы.


matrix = [[53, 91, 58, 44, 88, 29],
          [95, 64, 77, 11, 44, 11],
          [83, 34, 55, 85, 91, 54],
          [91, 55, 23, 99, 36, 20]
          ]

list_min_nums = []
for i in range(len(matrix[0])):
    tpm_list = []
    for j in range(len(matrix)):
        tpm_list.append(matrix[j][i])
    list_min_nums.append(min(tpm_list))

print(f'Список минимальных элементов столбцов матрицы "matrix": {list_min_nums}')

max_num = list_min_nums[0]
for number in list_min_nums:
    if max_num < number:
        max_num = number

print(f'Максимальный элемент среди минимальных элементов столбцов матрицы "matrix": {max_num}')
