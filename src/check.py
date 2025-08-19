import random

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