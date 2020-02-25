num=int(input())
country={}
town=[]
for i in range(num):
    i=input().split()
    country[i[0]]=(i[1:])
num2=int(input())
for i in range(num2):
    i=input()
    town.append(i)
for i in range(len(town)):
    for x in country:
        if town[i] in country[x]:
            print(x)
