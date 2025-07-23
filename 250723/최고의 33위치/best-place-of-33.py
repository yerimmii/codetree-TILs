n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def count_coin(size, x, y):
    cnt = 0
    
    for i in range(size):
        for j in range(size):
            cnt += grid[x+i][y+j]
    return cnt

max_cnt = 0
for i in range(n-2):
    cnt = 0
    for j in range(n-2):
        max_cnt = max(max_cnt, count_coin(3, i, j)) 

print(max_cnt)