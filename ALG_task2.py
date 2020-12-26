import  random, re, math

#линейная
def func1(a):
    return min(a)

#квадратичная
def func2(a):
    mins = a[0]
    for i in a[1::]:
        if i < mins:
            mins = i
    return(mins)



a = [random.randint(-10, 10) for i in range(10)]
print(a)
print(func1(a))
print(func2(a))