def generate_numbers(n):
    for i in range(n):
        yield i

x= generate_numbers(5)
print(x)


