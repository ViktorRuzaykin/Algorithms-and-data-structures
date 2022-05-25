# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не
# должна завершаться, а должна запрашивать новые данные для вычислений. Завершение
# программы должно выполняться при вводе символа '0' в качестве знака операции. Если
# пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об
# ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности
# деления на ноль, если он ввел 0 в качестве делителя.

# Вариант 1
"""while True:
    try:
        user_data = input('Введите данные для вычислений. Для выхода введите "0": ')
        if user_data == '0':
            print('0')
            break
        else:
            print(eval(user_data))
    except (NameError, SyntaxError):
        print('Не корректные данные')

    except ZeroDivisionError:
        print('На ноль делить нельзя!')"""

# Вариант 2
import re

while True:
    user_data = input('Введите данные для вычислений. Для выхода введите "0": ')
    if user_data != '0':
        try:
            t = re.search(r'[*/+-]', user_data)[0]  # ищем в строке арифметический знак
            list_numbers = re.split(r'[+*/-]', user_data)  # получаем цифры из строки
            number_1 = list_numbers[0]
            number_2 = list_numbers[1]

            if t == '/':
                result = float(number_1) / float(number_2)
                print(result)

            if t == '*':
                result = float(number_1) * float(number_2)
                print(result)

            if t == '+':
                result = float(number_1) + float(number_2)
                print(result)

            if t == '-':
                result = float(number_1) - float(number_2)
                print(result)
        except (NameError, SyntaxError, ZeroDivisionError, ValueError, TypeError):
            print('Не корректные данные')
            continue
    else:
        break
