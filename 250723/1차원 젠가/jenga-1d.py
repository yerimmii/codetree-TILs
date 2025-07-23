n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

def remove_blocks(s, e):
    s, e = s-1, e-1
    temp = []
    for i in range(len(blocks)):
        if s <= i <= e:
            continue
        temp.append(blocks[i])
    return temp

blocks = remove_blocks(s1, e1)
blocks = remove_blocks(s2, e2)

size = len(blocks)
print(size)
for i in range(size):
    print(blocks[i])