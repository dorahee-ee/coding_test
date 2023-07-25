directions = input()

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0

move_dir = 0
cnt = 0
for direction in directions:
    if direction == 'L':
        move_dir = (move_dir - 1 + 4) % 4
    elif direction == 'R':
        move_dir = (move_dir + 1) % 4
    else:
        x, y = x + dxs[move_dir], y + dys[move_dir]
    
    cnt += 1
    if x == 0 and y == 0:
        print(cnt)
        break

if x != 0 and y != 0:
    print(-1)