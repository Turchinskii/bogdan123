countDict={}
human=0
while human!='\n':
    human=input().split()
    countDict[human[0]]=countDict.get(human[0],0)+int(human[1])
    human=input().split()
print(countDict)
