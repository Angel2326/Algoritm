"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""
import timeit


def simple(i2):  # итого :  O(N^2)
    """Без использования «Решета Эратосфена»"""
    count = 1  # O(1)
    n = 2  # O(1)
    while count <= i2:  # O(N)
        t = 1  # O(1)
        is_simple = True  # O(1)
        while t <= n:  # O(N)
            if n % t == 0 and t != 1 and t != n:  # O(1)
                is_simple = False  # O(1)
                break  # O(1)
            t += 1  # # O(1)
        if is_simple:  # O(1)
            if count == i2:  # O(1)
                break  # O(1)
            count += 1  # # O(1)
        n += 1  # # O(1)
    return n  # O(1)


def resheto_eratosphena(i1):  # итого :  O(N*LogN) + O(N) = O(N*LogN)
    n = i1 * 10  # O(1)
    a = [k for k in range(n + 1)]  # O(1)
    a[1] = 0  # O(1)
    m = 2  # O(1)
    while m < n:  # O(N*LogN) включая второй подцикл while
        if a[m] != 0:
            j = m * 2
            while j <= n:
                a[j] = 0
                j = j + m
        m += 1
    # Превращая список во множество,
    # избавляемся от всех нулей кроме одного.
    a = set(a)  # O(N)
    # удаляем ноль
    a.remove(0)  # O(1)
    # сортируем по возрастанию
    a = sorted(list(a))  # O(1)
    return a[i1 - 1]  # O(1)


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(resheto_eratosphena(i))
print(timeit.timeit("simple(i)", setup="from __main__ import simple,i", number=100))
print(timeit.timeit("resheto_eratosphena(i)", setup="from __main__ import resheto_eratosphena,i", number=100))

"""
Аналитика
При малых i (i=10) алгоритм "Решето эратосфена" проигрывает
С увеличением i на порядок наблюдаем все большее превосходство алгоритма "Решето эратосфена". А эффект этот
получается за счет того, что алгоритм "Решето эратосфена" работает в циклах while только c непростыми числами.
Обнуляются из списка все числа от 2p (где p - простое число) до n, делящиеся на p (то есть, числа 2p, 3p, 4p, …). 
Поэтому сложность алгоритма "Решето эратосфена" = O(N*LogN), у simple = O(N^2)

i=10
simple(i) = 0.0074277820000006045
resheto_eratosphena(i) = 0.009305418000000287

i=100
simple(i) = 0.827584614
resheto_eratosphena(i) = 0.12315412199999987

i=1000
simple(i) = 132.173610684
resheto_eratosphena(i) = 1.31301006999999

"""