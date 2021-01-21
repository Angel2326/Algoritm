"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit
from itertools import groupby
from collections import Counter


array = [1, 3, 3, 3, 4, 5, 1, 5, 8, 9, 6, 3, 4, 2, 5, 6, 7, 8, 9, 6, 343]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    v = {x: array.count(x) for x in array}
    for key in v:
        if v[key] == max(v.values()):
            return f'Чаще всего встречается число {key}, ' \
                   f'оно появилось в массиве {v[key]} раз(а)'
            break


def func_4():
    v = Counter(array)
    for key in v:
        if v[key] == max(v.values()):
            return f'Чаще всего встречается число {key}, ' \
                   f'оно появилось в массиве {v[key]} раз(а)'
            break

def func_5():
    v = max(array, key = array.count)
    return f'Чаще всего встречается число {v}, ' \
                   f'оно появилось в массиве {array.count(v)} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())
print(func_5())

print("func_1()")
print(timeit.timeit("func_1()", setup="from __main__ import func_1", number=100000))
print("func_2")
print(timeit.timeit("func_2", setup="from __main__ import func_2", number=100000))
print("func_3")
print(timeit.timeit("func_3", setup="from __main__ import func_3", number=100000))
print("func_4")
print(timeit.timeit("func_4", setup="from __main__ import func_4", number=100000))
print("func_5")
print(timeit.timeit("func_5", setup="from __main__ import func_5", number=100000))

"""
Замеры:
func_1()
2.545556558
func_2
0.003996316000000277
func_3
0.003914031999999956
func_4
0.0039039270000000847
func_5
0.0039635950000000975

Process finished with exit code 0

Нестабильно, но func_3 и func_2 практически рядом. Они быстрее чем func_5


"""