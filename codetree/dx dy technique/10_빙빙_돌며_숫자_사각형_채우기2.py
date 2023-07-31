n, m = tuple(map(int, input().split()))
answer = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
x, y = 0, 0
dir_num = 0 # 0: 아래, 1: 오, 2: 위, 3: 왼

answer[x][y] = 1

for i in range(2, n * m + 1):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if not in_range(nx, ny) or answer[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
    
    x, y = x + dxs[dir_num], y + dys[dir_num]
    answer[x][y] = i

# 출력:
for i in range(n):
    for j in range(m):
        print(answer[i][j], end = ' ')
    print()