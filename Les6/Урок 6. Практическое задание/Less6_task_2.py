"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from timeit import default_timer
from memory_profiler import profile

@profile
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


@profile
def resheto_eratosphena(i1):
    n = i1 * 10
    a = [k for k in range(n + 1)]
    a[1] = 0
    m = 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j <= n:
                a[j] = 0
                j = j + m
        m += 1
    # Превращая список во множество,
    # избавляемся от всех нулей кроме одного.
    a = set(a)
    # удаляем ноль
    a.remove(0)
    # сортируем по возрастанию
    a = sorted(list(a))
    return a[i1 - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(resheto_eratosphena(i))

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     9     14.6 MiB     14.6 MiB           1   @profile
    10                                         def simple(i):
    11                                             """Без использования «Решета Эратосфена»"""
    12     14.6 MiB      0.0 MiB           1       count = 1
    13     14.6 MiB      0.0 MiB           1       n = 2
    14     14.7 MiB      0.0 MiB        1986       while count <= i:
    15     14.7 MiB      0.0 MiB        1986           t = 1
    16     14.7 MiB      0.0 MiB        1986           is_simple = True
    17     14.7 MiB      0.0 MiB      278385           while t <= n:
    18     14.7 MiB      0.0 MiB      278085               if n % t == 0 and t != 1 and t != n:
    19     14.7 MiB      0.0 MiB        1686                   is_simple = False
    20     14.7 MiB      0.0 MiB        1686                   break
    21     14.7 MiB      0.0 MiB      276399               t += 1
    22     14.7 MiB      0.0 MiB        1986           if is_simple:
    23     14.7 MiB      0.0 MiB         300               if count == i:
    24     14.7 MiB      0.0 MiB           1                   break
    25     14.7 MiB      0.0 MiB         299               count += 1
    26     14.7 MiB      0.0 MiB        1985           n += 1
    27     14.7 MiB      0.0 MiB           1       return n


1987
Filename: D:/GeekBrains/Python/Algoritm/Les6/Урок 6. Практическое задание/task_2.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     14.7 MiB     14.7 MiB           1   @profile
    31                                         def resheto_eratosphena(i1):
    32     14.7 MiB      0.0 MiB           1       n = i1 * 10
    33     14.8 MiB      0.0 MiB        3004       a = [k for k in range(n + 1)]
    34     14.8 MiB      0.0 MiB           1       a[1] = 0
    35     14.8 MiB      0.0 MiB           1       m = 2
    36     14.8 MiB      0.0 MiB        2999       while m < n:
    37     14.8 MiB      0.0 MiB        2998           if a[m] != 0:
    38     14.8 MiB      0.0 MiB         430               j = m * 2
    39     14.8 MiB      0.0 MiB        6846               while j <= n:
    40     14.8 MiB      0.0 MiB        6416                   a[j] = 0
    41     14.8 MiB      0.0 MiB        6416                   j = j + m
    42     14.8 MiB      0.0 MiB        2998           m += 1
    43                                             # Превращая список во множество,
    44                                             # избавляемся от всех нулей кроме одного.
    45     14.8 MiB      0.0 MiB           1       a = set(a)
    46                                             # удаляем ноль
    47     14.8 MiB      0.0 MiB           1       a.remove(0)
    48                                             # сортируем по возрастанию
    49     14.8 MiB      0.0 MiB           1       a = sorted(list(a))
    50     14.8 MiB      0.0 MiB           1       return a[i1 - 1]


1987

Инкримент нулевой, оптимизации не требуется

"""