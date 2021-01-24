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
    while n < len(lst_obj):
        count = 0
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
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))
orig_list = [random.randint(-100, 100) for _ in range(100)]
#
# # замеры 100
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))
#
orig_list = [random.randint(-100, 100) for _ in range(10000)]
#
# # замеры 10000
print(timeit.timeit("bubble_sort(orig_list)", \
                    setup="from __main__ import bubble_sort, orig_list", number=1))

orig_list = [random.randint(-100, 100) for _ in range(10)]
print('Замеры по убыванию')
# замеры 10
print(timeit.timeit("bubble_sort2(orig_list)", \
                    setup="from __main__ import bubble_sort2, orig_list", number=1))
orig_list = [random.randint(-100, 100) for _ in range(100)]
# # замеры 100
print(timeit.timeit("bubble_sort2(orig_list)", \
                    setup="from __main__ import bubble_sort2, orig_list", number=1))
orig_list = [random.randint(-100, 100) for _ in range(10000)]
# # замеры 10000
print(timeit.timeit("bubble_sort2(orig_list)", \
                    setup="from __main__ import bubble_sort2, orig_list", number=1))

""""
[-19, -79, 72, -47, 85, -58, -53, -11, 75, 18]
По возростанию
[-79, -58, -53, -47, -19, -11, 18, 72, 75, 85]
По убыванию
[-19, -79, 72, -47, 85, -58, -53, -11, 75, 18]
Замеры По возростанию
4.6195000000005815e-05
0.003186016
33.062523098
Замеры по убыванию
2.8389999997102677e-05
0.0001616830000017444
0.02972315699999939

Оптимизация дала результаты и теперь гораздо быстрее работает 0,0297 сек  против 33,06 сек
========================================

[52, -28, 18, -45, 21, -60, -26, 10, -95, 46]
По возростанию
[-95, -60, -45, -28, -26, 10, 18, 21, 46, 52]
По убыванию
[52, -28, 18, -45, 21, -60, -26, 10, -95, 46]
Замеры По возростанию
4.8118999999999246e-05
0.003919361999999996
17.026859544 (здесь предварительно отсортировал по возростанию)
Замеры по убыванию
3.6089999998267785e-05
0.00015879600000090477
0.01811279700000057 (здесь предварительно отсортировал по убыванию)




"""
