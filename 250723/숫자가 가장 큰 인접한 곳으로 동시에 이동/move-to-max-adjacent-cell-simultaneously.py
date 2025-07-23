n, m, t = map(int, input().split())
# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0] for pos in marbles]
c = [pos[1] for pos in marbles]

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y) -> tuple[int, int]:
    max_x, max_y = x, y
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if (in_range(nx, ny) and a[nx][ny] > a[max_x][max_y]):
            max_x, max_y = nx, ny
    return max_x, max_y

for _ in range(t):
    # 구슬 이동
    next_count = [tuple() for _ in range(len(marbles))]
    for i in range(len(marbles)):
        row, colm = r[i]-1, c[i]-1
        nx, ny = move(row, colm)
        next_count[i] = (nx, ny)

    cnt = {}
    for x in next_count:
        if x in cnt:
            cnt[x] += 1
        else:
            cnt[x] = 1
    
    next_count = [x for x in next_count if cnt[x] == 1]

    marbles = next_count
    r = [pos[0] for pos in marbles]
    c = [pos[1] for pos in marbles]

print (len(marbles))