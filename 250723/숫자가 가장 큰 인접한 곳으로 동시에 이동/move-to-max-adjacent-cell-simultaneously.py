n, m, t = map(int, input().split())
# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y) -> tuple[int, int]:
    max_x, max_y = x, y
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if (in_range(nx, ny) and a[nx][ny] > a[max_x][max_y]):
            max_x, max_y = nx, ny
    return (max_x, max_y)

for _ in range(t):
    # 구슬 이동
    next_count = [move(x, y) for (x, y) in marbles]
    
    cnt = {}
    for pos in next_count:
        cnt[pos] = cnt.get(pos, 0) + 1
    marbles = [pos for pos in next_count if cnt[pos] == 1]

print (len(marbles))