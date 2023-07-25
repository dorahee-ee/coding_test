n, t = map(int, input().split())
r, c, d = input().split()

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
mapper = {
    'R': 0,
    'D': 1,
    'U': 2,
    'L': 3
}
x, y, move_dir = int(r) - 1, int(c) - 1, mapper[d]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        move_dir = 3 - move_dir  # 방향전환

print(x + 1, y + 1)