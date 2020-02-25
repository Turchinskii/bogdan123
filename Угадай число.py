Avgust = int(input())
numbers_Avgust = set([i for i in range(Avgust)])
while True:
    numbers = input()
    if numbers == 'HELP':
        break
    else:
        otvet = input()
        numbers = set(map(int, numbers.split()))
        print(numbers)
        if otvet == 'YES':
            numbers_Avgust.intersection_update(numbers)
        else:
            numbers_Avgust.difference_update(numbers)
for i in numbers_Avgust:
    print(i)
