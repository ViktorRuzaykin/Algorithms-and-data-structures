# Определить, является ли год, который ввел пользователем, високосным или не високосным.

# user_year = int(input('Введите год: '))
user_year = int('1904')

if user_year % 4 == 0:
    if user_year % 100 == 0:
        if user_year % 400 == 0:
            print(f'{user_year} -  високосный год.')
        else:
            print(f'{user_year} -  не високосный год.')
    else:
        print(f'{user_year} -  високосный год.')
else:
    print(f'{user_year} -  не високосный год.')
