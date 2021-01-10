"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


"""замеры времени выполнения кода с помощью модуля timeit"""
if __name__ == '__main__':
    nums_user = [4, 6, 8, 9, 13, 24, 35, 65, 45, 54, 32, 21, 2, 4, 6]
    print(timeit.timeit("func_1(nums_user)", setup="from __main__ import func_1, nums_user", number=10000))
    print(timeit.timeit("func_2(nums_user)", setup="from __main__ import func_2, nums_user", number=10000))
    print(func_1(nums_user))
    print(func_2(nums_user))

"""
АНАЛИТИКА: 
func_1
0.065321916
func_2
0.05275403100000001
Упростил код до одной строки (через генераторное выражение) и по замерам видно, что стало быстрее (0.05275403100000001 
против 0.065321916). Уменьшил количество команд
"""
