with open('../input.txt', 'r', encoding='UTF-8') as input_file2:
    grade9=[]
    grade10=[]
    grade11=[]
    for line in input_file2.readlines():
        record=line.split()
        if int(record[2])==9:
            grade9.append(int(record[3]))
        if int(record[2])==10:
            grade10.append(int(record[3]))
        if int(record[2])==11:
            grade11.append(int(record[3]))
    if len(grade9)>1:
      grade_9=sum(grade9)/len(grade9)
    else:
      grade_9=int(grade9)
      grade_9=float(grade_9)
    if len(grade10)>0:
      grade_10=sum(grade10)/len(grade10)
    else:
      grade_10=int(grade_10)
      grade_10=float(grade_10)
    if len(grade11)>0:
      grade_11=sum(grade11)/len(grade11)
    else:
      grade_11=int(grade10)
      grade_11=float(grade_11)
    print(round(grade_9,10),round(grade_10,10),round(grade_11,10))