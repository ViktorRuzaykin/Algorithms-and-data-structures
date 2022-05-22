import random
import statistics


def median_main(array_random):
    arr = array_random
    len_arr = len(arr)
    if len_arr == 0:
        return 'Нет медианы для пустых данных'

    for i in range(len(arr)):
        if len(arr) == 2 and len_arr % 2 != 1:
            return (arr[0] + arr[1]) / 2
        if len(arr) != 1:
            min_num = min(arr)
            max_num = max(arr)
            arr.remove(min_num)
            arr.remove(max_num)
    return arr[0]


m = 4
array = [random.randint(0, 500) for _ in range(2 * m + 1)]
print(array)


print(f'function statistics.median - {statistics.median(array)}') # для проверки, что функция median_main выводит верное значение медианы
print(f"median_main - {median_main(array)}")
