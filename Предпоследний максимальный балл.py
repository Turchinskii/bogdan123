with open('../file3.txt', 'r', encoding='UTF-8') as input_file1:
    class9=[]
    class10=[]
    class11=[]
    posl_max9=0
    posl_max10=0
    posl_max11=0
    for line in input_file1.readlines():
        line=line.split()
        if int(line[2])==9:
            class9.append(int(line[3]))
        if int(line[2])==10:
            class10.append(int(line[3]))
        if int(line[2])==11:
            class11.append(int(line[3]))
    max9=max(class9)
    max10=max(class10)
    max11=max(class11)
    for i in range(len(class9)):
        if class9[i]<max9:
            posl_max9=class9[i]
    for i in range(len(class11)):
        if class11[i]<max11:
            posl_max11=class11[i]
    for i in range(len(class10)):
        if class10[i]<max10:
            posl_max10=class10[i]
    print(posl_max9,posl_max10,posl_max11)