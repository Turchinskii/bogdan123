N, M = list(map(int, input().split()))
Anna = set()
Boris = set()
for i in range(N):
    Anna.add(int(input()))
for i in range(M):
    Boris.add(int(input()))
print(len(Anna & Boris))
print(*sorted(Anna & Boris))
print(len(Anna - Boris))
print(*sorted(Anna - Boris))
print(len(Boris - Anna))
print(*sorted(Boris - Anna))