a = [1, 2, 3, 1, 2, 4, 3, 3, 4, 5, 5, 3, 4, 5, 4, 5, 3, 6, 7, 4, 6, 7, 7, 8, 6, 8, 8, 9, 7, 9]
b = {}
for i in a:
    if i not in b:
        b[i] = 1
    else:
        b[i] += 1

print(b)
print(a.count(3))