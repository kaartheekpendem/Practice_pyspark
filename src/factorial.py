def fact(a):
    c=1
    while a>=1:
        c=c*a
        a=a-1
    return c

def main(a):
    b= fact(a)
    return b

if __name__=="__main__":
    a=int(input())
    print(main(a))



