a =[1,2,3,4,5,3,2,11,44,5,43,34,5]
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



