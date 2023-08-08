def solution(cards1, cards2, goal):
    flag = True
    i, j = 0, 0
    for g in goal:
        if i < len(cards1):
            if cards1[i] == g:
                i += 1
                continue
        if j < len(cards2):
            if cards2[j] == g:
                j += 1
                continue
        flag = False
        break
    if flag:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))

# 깔끔한 풀이
'''
def solution(cards1, cards2, goal):
    for g in goal:
        if len(cards1) > 0 and g == cards1[0]:
            cards1.pop(0)       
        elif len(cards2) >0 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"
'''