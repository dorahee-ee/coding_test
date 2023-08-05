n = int(input())
data = list(map(int, input().split()))

sum_data = sum(data)
check = n * (n+1)// 2

result = check - sum_data
print(result)