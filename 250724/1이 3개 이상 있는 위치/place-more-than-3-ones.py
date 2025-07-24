n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def count(x, y):
    cnt = 0
    for dx, dy in dxy:
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny]:
            cnt += 1
    
    return True if cnt >= 3 else False

result = 0
for i in range(n):
    for j in range(n):
        if count(i, j):
            result += 1

print (result)