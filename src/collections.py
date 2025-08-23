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


