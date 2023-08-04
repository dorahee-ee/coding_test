n, m = map(int, input().split())
x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

curr_dir = d
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
flag = True

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

total_cnt = 0
while flag:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if arr[x][y] == 0:
        arr[x][y] = 1
        total_cnt += 1
    
    move_dir = (curr_dir + 2) % 4
    nx, ny = x + dx[move_dir], y + dy[move_dir]

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and arr[nx][ny] == 1:
            cnt += 1
    if cnt == 4:
        print('2-1')
        # 2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
        move_dir = (curr_dir + 2) % 4
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if in_range(nx, ny):
            x, y = nx, ny
            continue
        # 2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
        else:
            break
    
    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    else:
        print('3')
        # 3-1. 반시계 방향으로 90도 회전한다.
        curr_dir = (curr_dir - 1 + 4) % 4
        # 3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        print('break')
        continue
        if in_range(nx, ny):
            print('aaaaa')
            x, y = nx, ny
            break
        continue

print(total_cnt)