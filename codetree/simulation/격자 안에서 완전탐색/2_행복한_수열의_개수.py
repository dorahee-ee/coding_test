n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

if len(arr) == 1:
    print(2)

else:
    total_cnt = 0
    for col in range(n):
        cnt = 1
        for row in range(n):
            if row == 0:
                continue
            if arr[col][row] == arr[col][row-1]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt >= m:
                total_cnt += 1
                break

    for row in range(n):
        cnt = 1
        for col in range(n):
            if col == 0:
                continue
            if arr[col][row] == arr[col-1][row]:
                cnt += 1
            else:
                cnt = 1
            
            if cnt >= m:
                total_cnt += 1
                break
    
    print(total_cnt)