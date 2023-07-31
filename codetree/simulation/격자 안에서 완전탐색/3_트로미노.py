n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def max_all_the_ways(col, row):
    if col + 1 < n:
        if row + 1 < n:
            a = arr[col][row] + arr[col+1][row] + arr[col+1][row+1]
            b = arr[col+1][row] + arr[col+1][row+1] + arr[col][row+1]
            c = arr[col][row] + arr[col][row+1] + arr[col+1][row+1]
            d = arr[col][row] + arr[col+1][row] + arr[col][row+1]
        else:
            a = arr[col][row] + arr[col+1][row]
            b = arr[col+1][row]
            c = arr[col][row]
            d = arr[col][row] + arr[col+1][row]
    else:
        if row + 1 < n:
            a = arr[col][row]
            b = arr[col][row+1]
            c = arr[col][row] + arr[col][row+1]
            d = arr[col][row] + arr[col][row+1]
        else:
            a = arr[col][row]
            b = 0
            c = arr[col][row]
            d = arr[col][row]
    
    if col + 2 < n:
        e = sum([arr[col]])