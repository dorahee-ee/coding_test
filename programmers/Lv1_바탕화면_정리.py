def solution(wallpaper):
    min_x, min_y, max_x, max_y = 50, 50, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if i < min_x:
                    min_x = i
                if j < min_y:
                    min_y = j
                if i > max_x:
                    max_x = i
                if j > max_y:
                    max_y = j

    return [min_x, min_y, max_x+1, max_y+1]

print(solution(	[".#...", "..#..", "...#."]))