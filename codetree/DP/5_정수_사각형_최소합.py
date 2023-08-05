n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][n-1] = arr[0][n-1]
for i in range(n-2, -1, -1):
    dp[0][i] = dp[0][i+1] + arr[0][i]
for i in range(1, n):
    dp[i][n-1] = dp[i-1][n-1] + arr[i][n-1]

for x in range(1, n):
    for y in range(n-2, -1, -1):
        dp[x][y] = min(dp[x-1][y], dp[x][y+1]) + arr[x][y]

print(dp[n-1][0])