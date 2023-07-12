def solution(a, b):
    c, d = max(a, b), min(a, b) # a, b 중 최대값과 최소값을 각각 c, d에 할당
    t = 1
    while t > 0:  # 유클리드 호제법(나머지 t가 0이 될 때까지)
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]  # 최소공배수 = 두 수의 곱 / 최소공배수

    return answer