import random

"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def rid(num, popytki):
    n = int(input('введите число: '))
    if popytki == 0:
        return print('попытки закончились')
    elif n == num:
        return print('число угадано ')
    else:
        if n > num:
            print('число больше случайного')
        else:
            print('число меньше случайного')
        return rid(num, popytki - 1)


number = random.randint(1, 100)
rid(number, 10)
