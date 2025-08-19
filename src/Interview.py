# Reversing a String using an Extended Slicing techniques.

a='kaartheek'
print(a[::-1])

#Count Vowels from Given words .
c=0

for i in a:
    if i in ['a','e','i','o','u']:
        c+=1
print(c)

#Find the highest occurrences of each word from string and sort them in order.

st = "apple banana apple orange banana apple"
d={}
for i in st.split():
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print([i for i ,j in d.items() if j == max(d.values())][0])

# Remove Duplicates from List

lst =[1,1,1,2,3,2,2,3,4,5,6,7,7,4]
print(list(set(lst)))
v=[]
for i in lst:
    if i in v:
        continue
    else:
        v.append(i)
print(v)


#Sort a List without using Sort keyword

srt = [3,2,4,2,45,54,2,1,2,44,5,32,2,21,33]
print(sorted(srt))
s=[]
"""
while srt:
    d = srt[0]             # Assume first element is the smallest
    for i in srt:          # Find the actual smallest element
        if i < d:
            d = i
    s.append(d)            # Add smallest to sorted list
    srt.remove(d)          # Remove it from original list

"""

for j in range(len(srt)):
    d = srt[0]             # Assume first element is the smallest
    for i in srt:          # Find the actual smallest element
        if i < d:
            d = i
    s.append(d)            # Add smallest to sorted list
    srt.remove(d)

print(s)


#Find the pair of numbers in this list whose sum is n no.

v=[2,7,11,15]

t=9

def tgt_num(v,t):
    d=[]
    for i in v:
        s = t - i
        if s in v:
            d.append(s)
    return d

z= tgt_num(v,t)
print(sorted(z))


#try to understand this code as well
def tgt_num(v, t):
    seen = set()
    pairs = []
    for i in v:
        s = t - i
        if s in seen:
            pairs.append((s, i))
        seen.add(i)
    return sorted(pairs)

# Example usage
v = [2, 7, 11, 15]
t = 9
z = tgt_num(v, t)
print(z)  # Output: [(2, 7)]


#Find the max and min no in the list without using inbuilt functions.

smrt = [3,2,4,2,45,54,2,1,2,44,5,32,2,21,33]
m=[]
while smrt:
    c = smrt[0]
    for i in smrt:
        if i < c:
            c=i
    m.append(c)
    smrt.remove(c)
print([m[0],m[-1]])


#Calculate the Intersection of Two Lists without using Built-in Functions
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7]
c=[]
for i in a :
    if i in b:
        c.append(i)

print(c)
















