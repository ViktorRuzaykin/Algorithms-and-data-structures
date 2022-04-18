# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# num = list(input('Введите трехзначное число: '))
num = '365'

result = 0

if len(num) == 3:
    for n in num:
        result += int(n)
    print(result)
else:
    print(f'Значение {"".join(num)} не трезначное!')
