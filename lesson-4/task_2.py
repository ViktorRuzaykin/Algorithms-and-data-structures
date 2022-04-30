import cProfile

n_user = 80000
m = [i for i in range(2, n_user + 1)]


def sieve_not():
    new_m = []
    for i in m:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            new_m.append(i)
    print(new_m)
    # Сложность этого алгоритма — O(n*2)


def sieve():
    new_m = []
    n = n_user
    sieve_set = set(range(2, n + 1))
    while sieve_set:
        prime = min(sieve_set)
        new_m.append(prime)
        sieve_set -= set(range(prime, n + 1, prime))
    print(new_m)
    # Сложность этого алгоритма — O(корень из n)


def main():
    sieve_not()
    sieve()


cProfile.run('main()')

"""
    Результаты профилировки двух функций sieve_not() и sieve()
    В сравнительном анализе видно, что функция sieve() выполняется быстрее функции sieve_not()
    примерно в 10 раза.
    Функция sieve_not() имеет квадратичную сложность O(n2). т.к. имеется вложеный цикл for.
    У функции sieve() сложность алгаритма O (корень из n).
    
    ncalls  tottime  percall  cumtime  percall ilename:lineno(function)
     1    0.000    0.000   17.778   17.778 <string>:1(<module>)
     1    0.035    0.035    1.670    1.670 task_2.py:19(sieve)
     1    0.001    0.001   17.778   17.778 task_2.py:31(main)
     1   16.085   16.085   16.107   16.107 task_2.py:7(sieve_not)
     1    0.000    0.000   17.778   17.778 {built-in method builtins.exec}
  7837    1.630    0.000    1.630    0.000 {built-in method builtins.min}
     2    0.023    0.012    0.023    0.012 {built-in method builtins.print}
 15674    0.003    0.000    0.003    0.000 {method 'append' of 'list' objects}
     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}"""
