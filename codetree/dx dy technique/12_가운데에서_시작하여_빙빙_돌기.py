n = int(input())
mid = n // 2
arr = [[0]*n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
x, y = mid, mid
dir_num = 0

arr[x][y] = 1
number = 2

while number < n*n + 1:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if in_range(nx, ny) and arr[nx][ny] == 0:
        arr[nx][ny] = number
        dir_num = (dir_num + 1) % 4
        x, y = nx, ny
        number += 1
    else:
        dir_num = (dir_num - 1 + 4) % 4

for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()