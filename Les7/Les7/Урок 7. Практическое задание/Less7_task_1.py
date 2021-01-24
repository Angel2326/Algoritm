"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

import random
import timeit


def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]


def bubble_sort2(lst_obj):
    n = 1
    count = 0
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                count += 1
            if count == 0:
                break
        n += 1
    return lst_obj


orig_list = [random.randint(-100, 100) for _ in range(10)]
print(orig_list)
print('По возростанию')
print(bubble_sort(orig_list[:]))
print('По убыванию')
print(bubble_sort2(orig_list[:]))

print('Замеры По возростанию')
# замеры 10
print(timeit.timeit("bubble_sort(orig_list[:])", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))
orig_list = [random.randint(-100, 100) for _ in range(100)]
#
# # замеры 100
print(timeit.timeit("bubble_sort(orig_list[:])", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))
#
orig_list = [random.randint(-100, 100) for _ in range(1000)]
#
# # замеры 10000
print(timeit.timeit("bubble_sort(orig_list[:])", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(10)]
print('Замеры по убыванию')
# замеры 10
print(timeit.timeit("bubble_sort2(orig_list[:])", \
                    setup="from __main__ import bubble_sort2, orig_list", number=1))
orig_list = [random.randint(-100, 100) for _ in range(100)]
# # замеры 100
print(timeit.timeit("bubble_sort2(orig_list[:])", \
                    setup="from __main__ import bubble_sort2, orig_list", number=1))
orig_list = [random.randint(-100, 100) for _ in range(1000)]
# # замеры 10000
print(timeit.timeit("bubble_sort2(orig_list[:])", \
                    setup="from __main__ import bubble_sort2, orig_list", number=1))

""""
[20, 14, -7, -65, -5, -25, 13, -11, -64, 98]
По возростанию
[-65, -64, -25, -11, -7, -5, 13, 14, 20, 98]
По убыванию
[20, 14, -7, -65, -5, -25, 13, -11, -64, 98]
Замеры По возростанию
7.025500000000517e-05
0.004712377999999989
0.500669347
Замеры по убыванию
0.000103457000000029
0.0038996340000000407
0.505647347

Эффекта от оптимизации нет
"""
