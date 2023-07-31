# 재귀함수에서 가장 중요한 요소는 '종료 조건'이다.
n = int(input())

def print_helloworld(n):
    if n == 0:
        return
    print_helloworld(n-1)
    print('HelloWorld')

print_helloworld(n)