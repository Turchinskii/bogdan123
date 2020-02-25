slovo=input().split()
countdict={}
min_povtor=0
for value in range(len(slovo)):
    countdict[slovo[value]]= countdict.get(slovo[value], 0) + 1
for value in sorted(countdict):
    if countdict[value]>min_povtor:
        min_povtor=countdict[value]
        max_povtor=value
print(max_povtor)