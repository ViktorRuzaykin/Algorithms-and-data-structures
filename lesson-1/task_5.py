# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

print('Ведите буквы английского алфавита')
# symbol_1 = input('Первая буква = ').lower()
# symbol_2 = input('Вторая буква = ').lower()
symbol_1 = 'h'
symbol_2 = 'W'

pos_symbol_1 = ord(symbol_1) - 96
pos_symbol_2 = ord(symbol_2) - 96
distance = abs(pos_symbol_1 - pos_symbol_2) - 1
print(f'Буква "{symbol_1}" {pos_symbol_1}-я в алфавите\n'
      f'Буква "{symbol_2}" {pos_symbol_2}-я в алфавите\n'
      f'Между буквами {distance} букв.')
