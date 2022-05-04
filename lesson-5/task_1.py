# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
import collections

date = collections.defaultdict()
n = int(input('Количество предприятий: '))

all_profit = 0
for i in range(n):
    name_company = input(f'Наименование {i + 1}-го предприятия: ')
    profit_company = float(input('Прибыль за 4 квартала: '))
    date[name_company] = profit_company
    all_profit += profit_company

average = all_profit / n

name_company_average_up = [up for up in date if date[up] > average]
name_company_average_down = [down for down in date if date[down] < average]

print(f'Средняя прибыль по всем компаниям - {average} \n'
      f'Компании с прибылью выше среднего - {name_company_average_up} \n'
      f'Компании с прибылью ниже среднего - {name_company_average_down}')
