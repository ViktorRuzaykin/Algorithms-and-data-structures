# Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа
# должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю
# ячейку строки. В конце следует вывести полученную матрицу.


column = 5
row = 4

matrix = []
for i in range(row):
    list_tmp = []
    print(f'Строка {i + 1}')
    for j in range(column):
        # num = j
        num = int(input('Введите число:'))
        list_tmp.append(num)
    list_tmp.append(sum(list_tmp))
    matrix.append(list_tmp)

for line in matrix:
    for n in line:
        print(n, end='  ')
    print()

print(matrix)
