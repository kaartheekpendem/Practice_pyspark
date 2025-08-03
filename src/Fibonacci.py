n =10
l=[]
for i in range(0,n):
    if i in (0,1):
        l.append(i)

    else:
        l.append(l[-1]+l[-2])

print(l)
