import cProfile
import sys

n_user = 20000
m = [i for i in range(2, n_user + 1)]


def sieve_not():
    new_m = [None] * len(m)
    c = 0
    for i in m:
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            new_m[c] = i  # new_m.append(i)
        c += 1
    print(*new_m)

    # Сложность этого алгоритма — O(n*2)


def sieve():
    new_m = [None] * len(m)
    n = n_user
    sieve_set = set(range(2, n + 1))

    t = 0
    while sieve_set:
        prime = min(sieve_set)
        new_m[t] = prime  # new_m.append(prime)
        sieve_set -= set(range(prime, n + 1, prime))
        t += 1
        print(f'sieve_set - in - {sys.getsizeof(set(range(prime, n + 1, prime)))}')
    # print(*new_m)
    # Сложность этого алгоритма — O(корень из n)


def main():
    sieve_not()
    sieve()


cProfile.run('main()')

"""
В функциях убрал метод "append"  и заранее определил размер списка "new_m", 
что бы упростить пространственную сложность.
 
функция sieve_not() 
    Временная сложность: O(n*2)
    Пространственная сложаность: О(1)
    Использование памяти: более эффективна, чем функция sieve() 
    
функция sieve() 
    Временная сложность: O(корень из n)
    Пространственная сложаность: О(1)
    Использование памяти: менее эффективна, чем функция sieve_not(), 
                                потому что при каждом прохождении цикла while создается новое множество чисел.  

OS - Windows 11
Version Python 3.10

"""
