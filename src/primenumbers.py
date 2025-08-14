def primenums(nums):
    c=[]
    for i in range(2,nums):
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                break
        else:
            c.append(i)
    x=sorted(set(c))
    return x

n=primenums(20)
print(n)