n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dict = {'W':0, 'S':1, 'N':2, 'E':3}
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]

x, y = 0, 0
for i in range(n):
    x += (dx[dict[dir[i]]] * dist[i])
    y += (dy[dict[dir[i]]] * dist[i])

print(x, y)