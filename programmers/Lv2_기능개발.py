def solution(progresses, speeds):
    answer = []
    while len(progresses) > 0:  # progresses가 비었다면 멈춘다.
        cnt = 0  # 배포된 기능의 개수 초기화
        while len(progresses) > 0 and progresses[0] >= 100:  # 해당 작업이 완료되어싸면 progresses와 speeds에서 제거하고 배포된 기능 개수를 증가시킨다.
            cnt += 1
            progresses.pop(0)
            speeds.pop(0)
        progresses = [progresses[i] + speeds[i] for i in range(len(progresses))]
        
        if cnt > 0: # 만약 오늘 배포된 기능 개수가 0이 아니라면 결과 리스트에 추가한다.
            answer.append(cnt)
    
    return answer