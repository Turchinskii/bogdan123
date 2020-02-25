a=int(input())
b=int(input())
c=int(input())
d=int(input())
one=[]
two=[]
s1=set()
s2=set()
one.append(a);one.append(b)
two.append(c);two.append(d)
max1=max(one);min1=min(one)
max2=max(two);min2=min(two)
for i in range(min1,max1+1):
    s1.add(i)
for i in range(min2,max2+1):
    s2.add(i)
print(len(s1&s2))
