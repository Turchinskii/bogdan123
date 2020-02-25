with open('../file2.txt', 'r', encoding='UTF-8') as input_file2:
    number_school=[]
    school_counter=[]
    for line in input_file2.readlines():
        record=(line.split())
        print(record)
        number_school.append(int(record[2]))
    school=set(number_school)
    school=list(school)
    print(number_school)
    for i in range(len(school)):
        school_counter.append(number_school.count(school[i]))
    print(school_counter)
    maximum=max(school_counter)
    maximum_ind=school_counter.index(maximum)
    print(school[maximum_ind],end=' ')
    school_counter.pop(maximum_ind)
    maximum2 = max(school_counter)
    if maximum2==maximum:
        maximum2 = school_counter.index(maximum2)
        print(school[maximum2 + 1])