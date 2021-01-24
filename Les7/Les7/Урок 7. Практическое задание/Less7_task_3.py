"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.


Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import random
import timeit
from statistics import median


def find_median1(lst):
    lst.sort()
    return lst[int((len(lst) - 1) / 2)]


def find_median2(lst):
    lst.sort()
    for _ in range(int(len(lst) // 2)):
        lst.pop(0)
    return min(lst)


def find_median3(lst):
    lst = sorted(lst)
    if len(lst) % 2 == 1:
        return lst[len(lst) // 2]
    else:
        return 0.5 * (lst[len(lst) // 2 - 1] + lst[len(lst) // 2])


def sorte(lst_num):
    for i in range(len(lst_num)):
        l = i
        for k in range(i + 1, len(lst_num)):
            if lst_num[k] < lst_num[l]:
                l = k
        lst_num[l], lst_num[i] = lst_num[i], lst_num[l]
    return lst_num


"""С сортировкой SHELL"""


def shell(lst):
    inc = len(lst) // 2
    while inc:
        for i, el in enumerate(lst):
            while i >= inc and lst[i - inc] > el:
                lst[i] = lst[i - inc]
                i -= inc
            lst[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return find_median1(lst)


""" без сортировки
"""


def quickselect_median(l, pivot_fn=random.choice):
    if len(l) % 2 == 1:
        return quickselect(l, int(len(l) / 2), pivot_fn)
    else:
        return 0.5 * (quickselect(l, int(len(l) / 2) - 1, pivot_fn) +
                      quickselect(l, int(len(l) / 2), pivot_fn))


def quickselect(l, k, pivot_fn):
    """
    Выбираем k-тый элемент в списке l (с нулевой базой)
    :param l: список числовых данных
    :param k: индекс
    :param pivot_fn: функция выбора pivot, по умолчанию выбирает случайно
    :return: k-тый элемент l
    """
    if len(l) == 1:
        assert k == 0
        return l[0]

    pivot = pivot_fn(l)

    lows = [el for el in l if el < pivot]
    highs = [el for el in l if el > pivot]
    pivots = [el for el in l if el == pivot]

    if k < len(lows):
        return quickselect(lows, k, pivot_fn)
    elif k < len(lows) + len(pivots):
        # Нам повезло и мы угадали медиану
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots), pivot_fn)


m = int(input('m = :'))
my_lst = [random.randint(-100, 100) for _ in range(2 * m + 1)]
print(shell(my_lst[:]))
print(timeit.timeit("shell(my_lst)", setup="from __main__ import shell, my_lst", number=1))

print(quickselect_median(my_lst[:]))
print('Поиск медианы без сортировки',
      timeit.timeit("quickselect_median(my_lst)", setup="from __main__ import quickselect_median, my_lst", number=1))

print(f'statistics.median(my_lst): {median(my_lst[:])}')
