"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""


class HexNumber:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return hex(int(self.x, 16) + int(other.x, 16))

    def __mul__(self, other):
        return hex(int(self.x, 16) * int(other.x, 16))

    def __sub__(self, other):
        return hex(int(self.x, 16) - int(other.x, 16))

    def __truediv__(self, other):
        return float.hex((int(self.x, 16) / int(other.x, 16)))

    def __str__(self):
        return str(list(str(self.x).upper()))

hx = HexNumber('A2')
hy = HexNumber('C4F')
print(f'Сумма = {HexNumber(hx + hy)}, Произведение = {HexNumber(hx * hy)}, Разность = {HexNumber(hx - hy)}, Частное = {HexNumber(hx / hy)}')
