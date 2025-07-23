n, r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y) -> tuple[int, int]:
    # 다음 위치 반환
    # 움직일 위치 없을 시 (-1, -1) 반환
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and a[nx][ny] > a[x][y]:
            return (nx, ny)
    return (-1, -1)

r, c = r-1, c-1
while True:
    print(a[r][c], end=' ')
    
    nx, ny = move(r, c)
    if (nx, ny) == (-1, -1):
        break
    r, c = nx, ny