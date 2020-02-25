with open('../input.txt', 'r') as input_file:
    spisok2={}
    for line in input_file.readlines():
        print(line.strip())
        line=line.split()
        spisok2[line[0]] =(line[1:])
    def telephone(name):
        for i in spisok2:
            if i in name:
                return (i+' '+' '.join(spisok2[i]))
    while 1!=0:
        name=input()
        print(telephone(name))











