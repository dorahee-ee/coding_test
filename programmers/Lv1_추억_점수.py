def solution(names, yearnings, photos):
    answer = []
    yearning_dict = {name:yearning for name, yearning in zip(names, yearnings)}
    for photo in photos:
        score = 0
        for p in photo:
            if p in yearning_dict:
                score += yearning_dict[p]
        answer.append(score)
    
    return answer