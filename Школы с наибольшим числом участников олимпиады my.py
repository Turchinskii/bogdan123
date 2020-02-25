with open('../file3.txt', 'r', encoding='UTF-8') as input_file1:
    people=[]
    for line in input_file1.readlines():
        people.append(line)
    people.sort()
    print(''.join(people))