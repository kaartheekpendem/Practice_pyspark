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
print(d)"""

a=[1,2,2,2,3,4,3,5,5,4,5,6,7,8,9,2,3,2,3,1]
"""b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

s= [(i,j) for i,j in b.items()]
s=sorted(s,key=lambda x:x[1],reverse=True)[:3]
print([i for i,j in s])"""
"""
a.pop(a[0])
print(a)

a={'s':1,'h':4}
b={'t':5,'h':3}
print(a|b)

c = {'n':4,'m':6,'g':4}
print(sorted(c.items(),key=lambda x:x[1],reverse=True))"""

j={
  "user": {
    "id": 101,
    "name": "Karthik",
    "address": {
      "city": "Fairfax",
      "zip": "22030"
    },
    "skills": ["python", "aws", "redshift"]
  }
}
"""

def fun(j):
    k={}
    for i ,m in j.items():
        if isinstance(m,dict):
            k.update(fun(m))
        else:
            k[i]=m
    return k

x= fun(j)
print(x)

d=dict(zip(["a","b","c"],[1,2,3]))
print(d)

from collections import namedtuple

Person = namedtuple("Person", ["name", "age"])
p = Person("Karthik", 30)
print(p.age)"""
"""
a=[1,2,3,4,5,4,3,2,2,2,2,4,5,6,7,2,3]
c={}
for i in a:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1

print(c)

import random

v=[random.randint(100,200) for i in range(10)]
print(v)"""


a=[1,2,3,4,5,4,3,2,2,2,2,4,5,6,7,2,3]
c={}
for i in a:
    if i not in c:
        c[i]=1
    else:
        c[i]+=1

print(c)

c.pop(7)
print(c)




