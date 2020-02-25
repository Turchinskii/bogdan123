synonym_dictionary={}
for synonyms in range(int(input())):
    synonym_1,synonyms_2=input().split()
    synonym_dictionary[synonym_1]=(synonyms_2)
find=input()
for i in synonym_dictionary:
    if i==find:
        print(synonym_dictionary[i])
    elif synonym_dictionary[i]==find:
        print(i)
    else:
        continue
