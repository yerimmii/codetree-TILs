n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

belt = u + d

for _ in range(t):
    temp = belt[-1]
    for i in range(2*n - 1, 0, -1):
        belt[i] = belt[i - 1]
    belt[0] = temp

for i in range(0, n):
    print(belt[i], end=' ')
print()
for i in range(n, 2*n):
    print(belt[i], end=' ')