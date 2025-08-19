"""a={'b':2,'c':3,'d':4}

print(a.keys())
print(a.values())
a.pop('c')
print(a)

a.setdefault('a',0)
print(dict(sorted(a.items())))

a.update({'a':4})
print(dict(sorted(a.items())))

for i,j in a.items():
    print(f"Here is key: {i} and here is value: {j}")

"""
"""
import random

n = [random.randint(100,200) for i in range(10)]
c=[]
for i in n:
    if i<100:
        c.append(i)
print(c)
"""

import random
a=[]
for i in range(10):
    n= random.randint(50,250)
    a.append(n)
print(a)

c=['below100','100to200','200above']
d = {k:[] for k in c}
print(d)
for i in a:
    if i<100:
        d['below100'].append(i)
    elif i in range(101,200):
        d['100to200'].append(i)
    else:
        d['200above'].append(i)
print(d)