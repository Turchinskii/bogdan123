distance=sorted([int(i) for i in input().split()]) #10 20 30
kilometr=sorted([int(i) for i in input().split()]) #50 20 30     #1700
kilometr.reverse()
summa=0
for i in range(len(distance)):
    oper1=(distance[i]*kilometr[i])
    summa+=oper1
print(summa)