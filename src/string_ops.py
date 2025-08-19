a='karthikkeerthi'
"""
print(list(a))

print(a[::-1])

print(''.join(list(a)))

print(''.join([i for i in list(a) if i !='k']))

print(a.index('e',2))

print(a.count('k'))

print(a.endswith('i'))

str = 'Hello World'

str = list(str.split())
m_str=[]
for i in str:
    m_str.append(i[::-1])


print(" ".join(m_str))


a=3
b=[3,5,2]
k=10

def max_candies(prices, budget):
    prices.sort()  # Sort prices ascending
    count = 0
    for price in prices:

        while budget >= price:
            print(budget)
            budget -= price
            count += 1
    print(budget)
    return count

# Prices: apple, orange, banana
prices = [4, 3, 8]
budget = 10

print("Maximum candies you can buy:", max_candies(prices, budget))"""

# when I need to split a string into separate variable in a list
print([i for i in a])

for i in a:
    if i =='a':
        a=a.replace(i,'l')

print(a)



a='kaartheek'
print(a[0:1])

c= 'i am here in virginia'

print(c.find('virginia'))


x = "Hello, World! Hello, Universe!"
print(x.rfind('Hello'))

x=x[:x.rfind('Hello')]+x[x.rfind('Hello'):].replace('Hello','karthik',1)
print(x)


print(list(a))