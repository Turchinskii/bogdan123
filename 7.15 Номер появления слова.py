with open('../input.txt', 'r') as input_file:
    slova=[]
    for line in input_file.readlines():
        print(line.strip())
        line=line.split()
        slova.append(line)
    countDict={}
    for i in range(len(slova)):
        for x in range(len(slova[i])):
            countDict[slova[i][x]] = countDict.get(slova[i][x], -1) + 1
            print(countDict[slova[i][x]])
