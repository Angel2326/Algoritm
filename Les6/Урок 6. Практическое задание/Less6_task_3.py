"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""

from memory_profiler import profile


@profile
def mem_time(num):
    def mirror(number, m=0):
        if number == 0:
            return print(f'Результат:{m}')
        else:
            return mirror(number // 10, m * 10 + number % 10)
    return mirror(num)


user_num = int(input('Введите число: '))
mem_time(user_num)

"""
Делаем внешнюю функцию, ее профилируем. Сама внешняя ф-ия вызывает уже рекурсию

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     14.8 MiB     14.8 MiB           1   @profile
    13                                         def mem_time(num):
    14     14.8 MiB      0.0 MiB           5       def mirror(number, m=0):
    15     14.8 MiB      0.0 MiB           4           if number == 0:
    16     14.8 MiB      0.0 MiB           1               return print(f' результат:{m}')
    17                                                 else:
    18     14.8 MiB      0.0 MiB           3               return mirror(number // 10, m * 10 + number % 10)
    19     14.8 MiB      0.0 MiB           1       return mirror(num)
"""