"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

import cProfile
import time
import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def general():
    revers(numb)
    revers_2(numb)
    revers_3(numb)


numb = 156783564645645646
cProfile.run("general()")
print("revers(numb)")
print(timeit.timeit("revers(numb)", setup="from __main__ import revers, numb", number=1000))
print("revers_2(numb)")
print(timeit.timeit("revers_2(numb)", setup="from __main__ import revers_2, numb", number=1000))
print("revers_3(numb)")
print(timeit.timeit("revers_3(numb)", setup="from __main__ import revers_3, numb", number=1000))

"""
Сделайте вывод, какая из трех реализаций эффективнее и почему

Для функций с малым временем исполнения cProfile не подходит, нужно использовать timeit

из трех реализаций эффективнее  revers_3(numb). Минимальное время на выполнение. 
revers_3(numb) имеет наименьшую сложность.


revers(numb)
3.12779999999957e-05
revers_2(numb)
2.2135000000006455e-05
revers_3(numb)
7.6989999999999e-06
"""
