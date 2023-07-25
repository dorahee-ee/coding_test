n = int(input())

x, y = 0, 0
# 동, 서, 남, 북순으로 dx, dy 정의
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]
mapper = {'E':0, 'W':1, 'S':2, 'N':3}

for i in range(n):
    move_dir, dist = input().split()
    dist = int(dist)
    move_dir = mapper[move_dir]

    # 주어진 방향대로 dist 거리만큼 이동
    x += dx[move_dir] * dist
    y += dy[move_dir] * dist

print(x, y)