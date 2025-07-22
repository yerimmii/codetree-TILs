command = input()

# N -> 0
# E -> 1
# S -> 2
# W -> 3
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

dir_num = 0
x, y = 0, 0

for c in command:
    if c == 'L':
        dir_num = (dir_num - 1) % 4
    elif c == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)