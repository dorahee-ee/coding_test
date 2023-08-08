def solution(keymaps, targets):
    answer = []

    for target in targets:
        ans = 0
        flag = True
        for t in target:
            click = []
            for keymap in keymaps:
                tmp = keymap.find(t)
                if tmp == -1:
                    continue
                else:
                    click.append(tmp+1)
            if not(click):
                ans = -1
                flag = False
            else:
                if flag:
                    ans += min(click)
                else:
                    ans = -1
        answer.append(ans)
    
    return answer

print(solution(["BC"], ["AC", "BC"])) # 반례