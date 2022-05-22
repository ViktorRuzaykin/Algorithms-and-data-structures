from random import randrange

l_not_sort = [randrange(-100, 100) for i in range(-20, 20)]
l_sort = [100, 98, 86, 85, 72, 69, 67, 54, 43, 42, 32, 31, 27, 22, 10, 9, 7, 3, 1, -13,
          -17, -18, -23, -27, -32, -35, -36, -43, -47, -49, -51, -59, -63, -71, -71, -76, -78, -84, -93, -98,
          ]


def sort_list(list_for_sort):
    flag = True
    l_s = list_for_sort
    n = 1
    while n < len(l_s):
        for i in range(len(l_s) - n):
            if l_s[i] < l_s[i + 1]:
                l_s[i], l_s[i + 1] = l_s[i + 1], l_s[i]
                flag = False
        if n == 1 and flag:
            return f'Этот список уже отсортирован'
        n += 1
    if flag is not True:
        return l_s


print(l_not_sort)
print(sort_list(l_not_sort))
print(l_sort)
print(sort_list(l_sort))
