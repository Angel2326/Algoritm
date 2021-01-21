"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!

"""
from timeit import default_timer
from memory_profiler import memory_usage


def mem_time(func):

    def wrapper(x):

        t1 = default_timer()
        m1 = memory_usage()
        func(x)
        t2 = default_timer()
        m2 = memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]
        print(f"Выполнение {func} заняло {round(time_diff,4)} сек and {mem_diff} Mib")
    return wrapper

@mem_time
def gen(numb):
    return [i for i in range(numb)]


@mem_time
def gen2(numb):
    a = []
    return a.append(range(numb))


@mem_time
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


@mem_time
def func1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr




if __name__ == '__main__':
    func1(range(100000))
    revers_3(range(100000))
    gen(100000)
    gen2(100000)


"""
Выполнение <function func1 at 0x02AC7778> заняло 0.1685 сек and 0.2890625 Mib
Выполнение <function revers_3 at 0x02AC7610> заняло 0.0996 сек and 0.0 Mib
Выполнение <function gen at 0x0062CAD8> заняло 0.111 сек and 0.75 Mib
Выполнение <function gen2 at 0x0062CBB0> заняло 0.1 сек and 0.0 Mib

Также укажите в комментариях версию Python и разрядность вашей ОС.
Python 3.8.5 / 64 бит разраядность
"""
