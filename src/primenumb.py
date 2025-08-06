n= 20
c=[]
for i in range(0,n):
    if i <=1:
        continue
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            break
    else:
        c.append(i)

print(c)


