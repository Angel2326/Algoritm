"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
import timeit
from collections import deque


def func1():
    for i in range(100):
        l.insert(0, i)
    return l


def func2():
    for i in range(100):
        d.appendleft(i)
    return d


def func3():
    for i in '12345':
        l.insert(0, i)
    return l


def func4():
    d.extendleft('12345')
    return d


def func5():
    for i in range(10):
        l.pop(0)
    return l


def func6():
    for i in range(10):
        d.popleft()
    return d


def func7():
    return l[5:10]


def func8():
    k = []
    for i in range(5):
        k.append(d[5+i])
    return k


s = range(1000)
l = list(s)
d = deque(s)

print("func1()", timeit.timeit("func1()", "from __main__ import func1", number=1000))
print("func2()", timeit.timeit("func2()", "from __main__ import func2", number=1000))
print()
print("func3()", timeit.timeit("func3()", "from __main__ import func3", number=1000))
print("func4()", timeit.timeit("func4()", "from __main__ import func4", number=1000))
print()
print("func5()", timeit.timeit("func5()", "from __main__ import func5", number=1000))
print("func6()", timeit.timeit("func6()", "from __main__ import func6", number=1000))
print()
print("func7()", timeit.timeit("func7()", "from __main__ import func7", number=1000))
print("func8()", timeit.timeit("func8()", "from __main__ import func8", number=1000))

"""
list отлично работает для нескольких операций, таких как индексация в списке.
Так получение элемента по индексу работает быстро, так как Python 
точно знает, где искать в памяти. Эта схема памяти также позволяет хорошо работать
со срезами списков.
Что касается deque, то отлично и быстро работает на концах списка, но плохо в середине

func1() 5.537446113000001
func2() 0.02300722799999999

func3() 0.5334608809999999
func4() 0.0007136079999998657

func5() 0.817579673
func6() 0.0028558739999997584

func7() 0.000490335000000286
func8() 0.003064710999999498
"""