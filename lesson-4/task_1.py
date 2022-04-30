# Определить, какое число в массиве встречается чаще всего.
import cProfile
from random import random

m = [int(random() * 100) for i in range(500000)]


def test_1():
    result_count = 0
    result_nums = 0
    set_m = set(m)
    for n in set_m:
        count = 0
        for j in m:
            if n == j:
                count += 1
                if count >= result_count:
                    result_count = count
                    result_nums = j
        #print(f'Число {n} повторяется {count} раз')

    print(f'Число {result_nums} встречается чаще всего - { result_count} раз.')
    # Сложность этого алгоритма — O(n)


def test_2():
    result_count = 0
    result_nums = 0
    set_m = set(m)
    for n in set_m:
        count = m.count(n)
        if count >= result_count:
            result_count = count
            result_nums = n
        #print(f'Число {n} повторяется {count} раз')

    print(f'Число {result_nums} встречается чаще всего - {result_count} раз.')


def main():
    test_1()
    test_2()


cProfile.run('main()')

"""
    Результаты профилировки двух функций test_1 и test_2
    В сравнительном анализе видно, что функция test_2 выполняется быстрее функции test_1
    примерно в 3 раза.
    Считаю что функция test_1 обладает квадратичной сложностью О(n2), а функция test_2 линейной сложностью. 
    Во втрой функции уже нет второго цикла for.
    Смею предположить т.к метод count, в функции test_2, встроенный метод языка Python, 
    поэтому функция test_2 она и работает быстре.  
    
    
    
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1    0.000    0.000    2.140    2.140 <string>:1(<module>)
     1    0.005    0.005    0.658    0.658 task_1.py:26(test_2)
     1    0.000    0.000    2.140    2.140 task_1.py:40(main)
     1    1.482    1.482    1.482    1.482 task_1.py:8(test_1)
     1    0.000    0.000    2.140    2.140 {built-in method builtins.exec}
     2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
   100    0.653    0.007    0.653    0.007 {method 'count' of 'list' objects}
     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""