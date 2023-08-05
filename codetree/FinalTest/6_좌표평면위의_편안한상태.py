n = int(input())
arr = [[0] * 1000 for _ in range(1000)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

coordinates = []

for _ in range(n):
    answer = 0
    x, y = map(int, input().split())
    arr[x][y] = 1
    coordinates.append((x, y))

    for xi, yi in coordinates:
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = xi + dx, yi + dy
            if in_range(nx, ny) and arr[nx][ny] == 1:
                cnt += 1

        if cnt == 3:
            answer += 1

    print(answer)
        