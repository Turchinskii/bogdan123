pupils=int(input())
languages=[]
spisok_1=[]
spisok_2=[]
num=0
num2=0
for i in range(pupils):
    pupil=int(input())
    for x in range(pupil):
        languages.append(input())
languages_pupils=set(languages)
languages_pupils=list(languages_pupils)
languages_pupils=languages_pupils[::-1]
for i in range(len(languages_pupils)):
    if languages.count(languages_pupils[i])==pupils:
        num+=1
        spisok_1.append(languages_pupils[i])
        spisok_2.append(languages_pupils[i])
        num2+=1
    else:
        num2+=1
        spisok_2.append(languages_pupils[i])
spisok_2=set(spisok_2)
spisok_2=list(spisok_2)
print(num)
print('\n'.join(spisok_1))
print(num2)
print('\n'.join(spisok_2))