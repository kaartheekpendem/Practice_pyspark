a={'b':2,'c':3,'d':4}

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