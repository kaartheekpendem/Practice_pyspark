a =[5,1,2,1,2,3,2,4,5,6,7,8,5,2,3,4]
b=set(a)

c =[8,10,11,12,12,13,14,16,15]
d =set(c)

print(b.union(d))
print(b.intersection(d))
print(b.difference(d))
print(d.difference(b))