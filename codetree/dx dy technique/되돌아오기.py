n = int(input())

x, y = 0, 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]
mapper = {
    'W' : 0,
    'S' : 1,
    'N' : 2,
    'E' : 3
}

cnt = 0
for _ in range(n):
    c_dir, dist = input().split()
    dist = int(dist)
    for _ in range(dist):
        move_dir = mapper[c_dir]
        x += dx[move_dir]
        y += dy[move_dir]
        cnt += 1
        if x == 0 and y == 0:
            print(cnt)
            break
    if x == 0 and y == 0:
        break

if x != 0 and y != 0:
    print(-1)