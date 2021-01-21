"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""
import timeit


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_2(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number  % 10)}{recursive_reverse_2(number  // 10)}'


def recursive_reverse_1(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number  % 10)}{recursive_reverse_1(number  // 10)}'


if __name__ == '__main__':
    nums_user = 4595
    print(timeit.timeit("recursive_reverse_2(nums_user)", setup="from __main__ import recursive_reverse_2, nums_user",
                        number=10000))
    print(recursive_reverse_2(nums_user))

    print(timeit.timeit("recursive_reverse_1(nums_user)", setup="from __main__ import recursive_reverse_1, nums_user",
                        number=10000))
    print(recursive_reverse_1(nums_user))

    """
    Для оптимизации алгоритма используем метод мемоизации (применяем в качестве декоратора), 
    то есть сохранение и повторное использование раннее вычисленных значений
    Как результат разница на прорядок 0.006209838000000002 против 0.060804445000000006 """
