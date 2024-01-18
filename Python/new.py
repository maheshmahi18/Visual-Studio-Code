def bs(a,b):
    c,d=0,len(a)-1
    while(c<=d):
        m=(c+d)//2
        mv=a[m]
        if mv==b:
            return m
        elif mv>b:
            c=m+1
        else:
            d=m-1
    return -1

a=eval(input())
b=int(input())
print(bs(a,b))