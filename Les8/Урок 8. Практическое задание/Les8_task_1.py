"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""
import heapq
from collections import Counter
from collections import namedtuple


class Sructure_Tree(namedtuple("Node", ["left", "right"])):
    def walk(self, code, symb):
        self.left.walk(code, symb + "0")
        self.right.walk(code, symb + "1")


class Leaf(namedtuple("Leaf", ["word"])):
    def walk(self, code, symb):
        code[self.word] = symb or "0"


def hafman_code(user_text):
    user_list = []
    for word, freq in Counter(user_text).items():
        user_list.append((freq, len(user_list), Leaf(word)))
    heapq.heapify(user_list)
    count = len(user_list)
    while len(user_list) > 1:
        freq1, _count1, left = heapq.heappop(user_list)
        freq2, _count2, right = heapq.heappop(user_list)
        heapq.heappush(user_list, (freq1 + freq2, count, Sructure_Tree(left, right)))
        count += 1
    code = {}
    if user_list:
        [(_freq, _count, root)] = user_list
        root.walk(code, "")
    return code


user_text = input("Введите строку: ")
code = hafman_code(user_text)
encoded = "".join(code[ch] for ch in user_text)
for ch in sorted(code):
    print("{}:{}".format(ch, code[ch]))
print(encoded)
