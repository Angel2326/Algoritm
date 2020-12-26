import random

class Stack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()       #удаляет элементы в порядке LIFO

    def size(self):
        return len(self.items)


    def is_empty(self):             #опустошает список
        return self.items == []

class Queue2Stacks(object):

    def __init__(self):

        # Two Stacks
        self.in_stack = Stack()
        self.out_stack = Stack()
        self.var_stack = Stack()


    def enqueue(self, item):
        self.in_stack.push(item)

    def pr_out(self):
        return self.in_stack.items


    def dequeue(self):
        if self.var_stack.is_empty:
            while self.in_stack.size()>0:
                while self.var_stack.size() < 4:  #порог
                    self.var_stack.push(self.in_stack.pop())
                self.out_stack.push(self.var_stack.items)
                self.var_stack.items=[]
            return  (self.out_stack.items)


#driver code
colour = [ "red", "blue", "green", "yellow", "purple", "orange", "white", "black" ]
q = Queue2Stacks()
for i in range(16):
    q.enqueue(random.choice(colour))
print(q.pr_out())
print(q.dequeue())