a=[1,2,1,2,2,3,4,2,2,3,4,2,3]
d = {}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i] =1

print(d)
max_key = max(d,key=d.get)
max_value = max(d.values())
print(f'here it is {max_key}:{max_value}')
