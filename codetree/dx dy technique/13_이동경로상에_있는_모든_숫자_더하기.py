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
