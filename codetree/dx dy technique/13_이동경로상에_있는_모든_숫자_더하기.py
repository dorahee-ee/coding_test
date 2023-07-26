'''# n, t = map(int, input().split())
# directions = input()
# arr = [list(map(int, input().split())) for _ in range(n)]
n, t = 5, 3
directions = 'FRL'
arr = [[6, 3, 3, 9, 1], [6, 3, 6, 1, 2], [7, 5, 2, 9, 8], [3, 2, 8, 5, 5], [9, 8, 9, 8, 1]]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = n//2, n//2

curr_dir = 0
total = arr[x][y]
for direction in directions:
    
    if direction == 'L':
        print(f'direction : {direction}')
        move_dir = (curr_dir - 1 + 4) % 4
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        print(arr[nx][ny])
        if in_range(nx, ny) == False:
            pass
        else:
            curr_dir = move_dir

    elif direction == 'R':
        print(f'direction : {direction}')
        move_dir = (curr_dir + 1) % 4
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        print(arr[nx][ny])
        if in_range(nx, ny) == False:
            pass
        else:
            curr_dir = move_dir

    else:
        print(f'direction : {direction}')
        nx, ny = x + dxs[curr_dir], y + dys[curr_dir]
        # print(arr[nx][ny])
        if in_range(nx, ny) == False:
            pass
        else:
            x, y = x + dxs[curr_dir], y + dys[curr_dir]
            total += arr[x][y]
            print(f'total : {total}')

# print(total)

'''

n, t = map(int, input().split())
directions = input()
arr = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
x, y = n//2, n//2

curr_dir = 0
total = arr[x][y]
for direction in directions:
    
    if direction == 'L':
        curr_dir = (curr_dir - 1 + 4) % 4

    elif direction == 'R':
        curr_dir = (curr_dir + 1) % 4

    else:
        if not in_range(x + dxs[curr_dir], y + dys[curr_dir]):
            continue
        x, y = x + dxs[curr_dir], y + dys[curr_dir]
        total += arr[x][y]

print(total)
