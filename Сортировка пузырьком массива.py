def marge(a,b):
    c=a+b
    for i in range(0,len(c)-1):
        for x in range(0,len(c)-1):
            if c[x]>c[x+1]:
                c[x],c[x+1]=c[x+1],c[x]
    return c
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
print(marge(A,B))