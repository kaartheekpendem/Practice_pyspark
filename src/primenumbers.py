def primenums(nums):
    c=[]
    for i in range(0,nums):
        if i in (1,2):
            continue
        for j in range(2,i):
            if i%j==0:
                break
            else:
                c.append(i)
    x=sorted(set(c))
    return x

n=primenums(20)
print(n)