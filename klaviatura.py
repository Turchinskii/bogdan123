number_of_keys=int(input()) #5
wear_key=[int(i) for i in input().split()] #1 50 3 4 3
number_of_keystrokes=int(input()) #16
sequence_pressed=[int(i) for i in input().split()] #1 2 3 4 5 1 3 3 4 5 5 5 5 5 4 5
wear_key2=[]
kl=[]
kl2=[]
sequence_pressed.sort()
for i in range(1,number_of_keys+1):
    kl.append(i)
for i in range(len(kl)):
    kl2.append(sequence_pressed.count(kl[i]))
for i in range(len(kl)):
    if kl[i]<kl2[i]:
        print('YES')
    else:
        print('NO')


