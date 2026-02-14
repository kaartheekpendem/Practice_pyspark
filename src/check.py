"""import random

a= []
for i in range(10):
    c= random.randint(100,300)
    a.append(c)

print(a)


d=['100below','100to200','200above']
b=[[],[],[]]
f=dict(zip(d,b))
print(f'here id {f}')
c= {k:[] for k in d}
print(c)

for i in a:
    if i<200:
        f['100to200'].append(i)
print(f)


s ='0'
print(int(s.strip()))


a='helloworldishere'

if 'world' in a:
    print('True')"""
from itertools import chain, product
a=[[1,2,3],[3,4,5,5],[6,7,5,4]]
m= list(chain.from_iterable(a))

v=['a','b','c']

l=list(product(a,v))

print(l)


from collections import Counter, defaultdict

c = Counter(m)
print(dict(c))

lst = defaultdict(list)
print(f'here is the list {lst}')
h=dict.fromkeys(v,[])
h['a']=[2]
h['a'].append(3)
print(h)

n= {'a':1,'b':2,'c':3}

logs = [
    ("2025-08-22", "User login"),
    ("2025-08-22", "File uploaded"),
    ("2025-08-23", "User logout"),
    ("2025-08-22", "Password changed"),
]

for i , j in logs:
    lst[i].append(j)
print({i:k for i,k in lst.items()})

from collections import deque
a=deque([1,2,3,4])
a.appendleft(6)
print(list(a))


a=123453
print(int(str(a)[::-1]))


# Parent class
class Vehicle:
    def start_engine(self):
        print("Engine started")

# Child class
class Car(Vehicle):
    def drive(self):
        print("Car is driving")

# Using the classes
my_car = Car()
my_car.start_engine()  # Inherited from Vehicle
my_car.drive()         # Defined in Car


def febi(n):
    a=[]
    for i in range(n):
        if i in (0,1):
            a.append(i)
        else:
            a.append(a[-1]+a[-2])
    return a

c=febi(10)
print(c)


a=[5,7,8,5,8,9,6,9,7,8]
print(a.index(9))

k= 'karthik'
print(k.capitalize())