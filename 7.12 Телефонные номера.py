num=input()
def telephone_nember(num):
    s=[]
    for i in range(len(num)):
        if num[i]!='+' or num[i]!='-':
            num[i]=int(num[i])
            return num[i]
print(telephone_nember(num))