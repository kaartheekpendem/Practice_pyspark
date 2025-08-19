"""import random
items = [1, 2, 3, 4]
random.shuffle(items)
print(items)

# Sample 3 unique elements from a list
print(random.sample(range(100), 3))"""
"""

import random

n = [random.randint(100,250) for _ in  range(10)]
print(n)

d ={}

for i in n:
    if i<100:
        d.setdefault('less100',[]).append(i)
    elif i in range(100,200):
        d.setdefault('100to200',[]).append(i)
    else:
        d.setdefault('200more',[]).append(i)

print(d)"""
"""
words = ["bat", "tab", "tap", "pat", "apt"]
# Output: {'abt': ['bat', 'tab'], 'apt': ['tap', 'pat', 'apt']}
output={}
for i in words:
    a=''.join(sorted(i))
    if a not in output:
        output.setdefault(a,[i])
    else:
        output[a].append(i)

print(output)
"""
"""
keys = ['a', 'b', 'c']
values = [1, 2, 3]
# Output: {'a': 1, 'b': 2, 'c': 3}

print(dict(zip(keys,values)))

"""
"""
nums = [1, 2, 3, 4, 2]
# Output: True (duplicate found)

d={}

for i in nums:
    if i not in d:
        d[i]=1
    else:
        del d[i]

print(d)"""
"""
nums = [1, 2, 3, 4, 2]
# Output: True (duplicate found)
d={}
for i in nums:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1

c={i:j for i, j in d.items() if j<2}
print(c)

c=d.pop(3)
print(d)
"""
"""
d = {'a': {'x': 1}, 'b': {'y': 2}}

# Output: {'a_x': 1, 'b_y': 2}
c={}
for i , j in d.items():
    for x,y in j.items():
        v=f"{i}_{x}"
        c[v]=y
print(c)
"""
"""
# TO GET VALUE OF THE KEY
k= {'a': 1, 'b': 2, 'c': 3}

print(k.get('a'))
"""







