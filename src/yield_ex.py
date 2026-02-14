"""def add(n):
    for i in range(n):
        yield i*2
a= add(4)
print(list(a))"""

def chunker(data, size):
    for i in range(0, len(data), size):
        yield data[i:i+size]

nums = list(range(20))

for chunk in chunker(nums, 5):
    print(chunk)



