from collections import OrderedDict

dic_comp = {'ООО НТ+': 100000,
              'ООО НТЭС': 500000,
              'ООО СПЕКТР': 4000000,
              'ООО СОЮЗ': 600000,
              'ООО Энергия': 800000,
              'ООО СНГ': 900000
            }
s = [(k, dic_comp[k]) #  O(1)
     for k in sorted(dic_comp, key=dic_comp.get, reverse=True)][:3] # O(N log N)
print(s) # O(1)

# O(N log N)*O(1)+ O(1)=(N log N + 1)



s = [(k, dic_comp[k]) for k in sorted(dic_comp, key=dic_comp.get, reverse=True)] # O(N log N)
output = OrderedDict() # O(N)
for k, v in s: #O(N)
    if k not in output: # O(N)
        output[k] = v #O(1)
        if len(output) == 3: #O(1)
            break #O(1)
print(output) #O(1)

# O(N log N)+O(N)*O(N)*(O(1)+O(1)*O(1))+O(1)=O(N log N +N^2+1)
# Первый вариант будет быстрее так как макс порядок у обоих выражений одинаковый, но у второго есть еще слагаемое второго порядка
