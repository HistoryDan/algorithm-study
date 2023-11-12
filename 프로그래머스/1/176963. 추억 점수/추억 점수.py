def solution(name, yearning, photo):
    answer = []
    ref = {}
    for i in range(len(name)):
        ref[name[i]] = yearning[i]
        
    for ph in photo:
        score = 0
        ph = set(ph)
        for p in ph:
            if p in ref:
                score += ref[p]
            else:
                continue
        answer.append(score)
        
    return answer