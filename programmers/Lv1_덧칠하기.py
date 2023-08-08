def solution(n, m, section):
    answer = 1
    loc = section[0]
    for sec in section:
        if loc + m <= sec:
            loc = sec
            answer += 1
    return answer