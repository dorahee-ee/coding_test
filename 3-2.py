# 배열의 크기 N, 숫자가 더해지는 횟수 M, 특정 인덱스의 최대 연속 덧셈 횟수 K
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse=True)

print(data)