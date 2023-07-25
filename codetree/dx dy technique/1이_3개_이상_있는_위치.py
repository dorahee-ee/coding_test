n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

total_cnt = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = j + dx, i + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            total_cnt += 1

print(total_cnt)