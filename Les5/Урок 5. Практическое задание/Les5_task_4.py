"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit
from collections import OrderedDict


def func1():
    keys = d.keys()
    keys = sorted(keys)
    for key in keys:
        print(key, d[key])


def func2():
    new_d = OrderedDict(sorted(d.items()))
    return new_d


def func3():
    return sorted(d, key=d.get, reverse=True)


def func4():
    new_d = OrderedDict(sorted(d.items()))
    for key in reversed(new_d):
        return new_d.keys()


def func5():
    (d["apricot"]) = 6
    return d


def func6():
    new_d = OrderedDict(d)
    new_d["apricot"] = "6"
    return new_d


d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2, 'avocado': 4}
print("func1()", timeit.timeit("func1()", "from __main__ import func1", number=1000))
print("func2()", timeit.timeit("func2()", "from __main__ import func2", number=1000))
print("func3()", timeit.timeit("func3()", "from __main__ import func3", number=1000))
print("func4()", timeit.timeit("func4()", "from __main__ import func4", number=1000))
print("func5()", timeit.timeit("func5()", "from __main__ import func5", number=1000))
print("func6()", timeit.timeit("func6()", "from __main__ import func6", number=1000))

"""
Класс collections.OrderedDict() используется для операций переупорядочивания, перемещения в конец и т.д, сортировка.
Если рассматривать сортировку только ключей, то обычный словарь dict выигрывает, если сортировка ключей со значениями то collections.OrderedDict() быстрее и проще
При Вставке новых ключей со значением преимущество за dict, 

func1() 0.083673978
func2() 0.00389139899999999

func3() 0.0016788789999999942
func4() 0.006511488999999981

func5() 0.0003580069999999935
func6() 0.002931902000000014

"""
