x='kaartheek'
c={}
for i in x:
    if i in c:
        c[i]+=1
    else:
        c[i]=1
print(c)
f=[]
for key, value in c.items():
    if value ==1:
        f.append(key)
print(f[0])

