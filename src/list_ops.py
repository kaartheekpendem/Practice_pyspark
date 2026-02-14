a=[]
for i,j in enumerate(range(10),0):
    print(i,j)
    a.append(j)

print(a)
b=a.extend([2,3])
print(a)
a.reverse()
print(a)
a.sort(reverse = True)
print(sorted(a,reverse= True))
"""a =[1,2,3,4,5,3,2,11,44,5,43,34,5]
x=sorted(a)
print(x)
print(sorted(a)[::-1])

z=[1,3,4,5,7,8]

for i in enumerate(z):
    print(i)
z.extend([3,5])
print(z)

z.remove(3)
print(z)

a.reverse()
print(a)

a.sort()
print(a)

v= [1,2,3]
u = [4,5,6]

print(v+u)

lst = v+u
print(sorted(set(lst))[::-1][1])


#recursive list

a= [1,[4,[6]]]

def list_ops(l,d=1):
    c=[]
    for i in l:
        if isinstance(i, int):
            c.append(i*d)
        elif isinstance(i,list):
            c.append(list_ops(i,d+1))
    return sum(c)

b= list_ops(a)
print(b)
"""


"""
import random
a =[1,2,3,4,5,3,2,11,44,5,43,34,5]

n= random.choices(a,k=3)
n= random.sample(a,5)
n = [a[random.randint(0,len(a)-1)] for i in range(5)]

print(n)

x=[3,4,5]

a.append(x)
a.extend(x)
print(a)
print(a)
"""
"""
from itertools import combinations
a =[-1,0,1,2,-1,-4,4,6,8,-9]
t=8
r=set()
for i in range(1,len(a)+1):
    for j in combinations(a,i):
        print(j)
        if sum(j) == t:
            r.add(tuple(j))

print(r)"""
"""
from collections import Counter, defaultdict, namedtuple, deque

# Counter
print(Counter('abracadabra'))  # {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}

# defaultdict
dd = defaultdict(int)
dd['missing'] += 1  # No KeyError
print(dd['o'])

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)

# deque
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.pop()"""

from collections import defaultdict


a=defaultdict(list)
b=[('mom',50),('mom',45),('dad',50)]
for i ,j in b:
    a[i].append(j)

print(a)



a='au'
d=[]
c=[i for i in a]
print(c)
x=[]
if not c:
    print(len(c))
for i in range(len(c)):
    if a[i] not in d:
        d.append(a[i])
        print(d)
    else:
        x.append(''.join(d))
        print(f'x is here: {x}')
        d=[a[i]]
    x.append(''.join(d))
print(x)
if not x:
    print(1)
else:
    print(len(max(x,key = len)))




def minimum_sum_with_integer_mean(N,A):
    S = sum(A)

    # If already divisible, no need to add anything
    if S % N == 0:
        return S

    # Otherwise, go to next multiple of N
    print(S%N)
    return S + (N - (S % N))


c= minimum_sum_with_integer_mean(4,[3,1,8,9])
print(c)


print(24%4)





