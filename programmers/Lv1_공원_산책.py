def solution(park, routes):
    def in_range(x, y):
        return 0 <= x and x < len(park) and 0 <= y and y < len(park[0])

    # 시작 위치 찾기
    flag = True
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j
                flag = False
                break
        if flag == False:
            break

    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
    mapper = {'E':0, 'W':1, 'S':2, 'N':3}
    
    for route in routes:
        direction, dist = route.split()
        dist = int(dist)
        move_dir = mapper[direction]
        curr_x, curr_y = x, y
        for _ in range(dist):
            nx, ny = curr_x + dx[move_dir], curr_y + dy[move_dir]
            if in_range(nx, ny) and park[nx][ny] != 'X':
                curr_x, curr_y = nx, ny
            else:
                curr_x, curr_y = x, y
                break
        x, y = curr_x, curr_y
                
    return [x, y]