"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time


def calc_time(function_to_decorate):
    start_time = time.time()
    function_to_decorate()
    return print("--- %s seconds ---" % (time.time() - start_time))


@ calc_time
def fill_dict():
    user_dict = {}
    for i in range(90000):
        user_dict[i] = i
    return print('user_dict')


@ calc_time
def fill_list():
    user_list = []
    for i in range(90000):
        user_list.append(i)
    return print('user_list')
