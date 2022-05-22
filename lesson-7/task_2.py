from random import randrange


def merge_two_list(a, b):
    c = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])
    rigth = merge_sort(s[middle:])
    return merge_two_list(left, rigth)


l_not_sort = [randrange(0, 50) for i in range(20)]
print(l_not_sort)
print(merge_sort(l_not_sort))
