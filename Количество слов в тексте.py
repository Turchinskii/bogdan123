with open('../slovo.txt', 'r') as input_file:
    a=[]
    b=[]
    for line in input_file.readlines():
        line=line.split()
        a.append(line)
    print(a)
    for i in range(len(a)):
        for x in range(len(a[i])):
            if a[i][x] not in b:
                b.append(a[i][x])
    print(len(b))