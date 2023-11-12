def solution(cards1, cards2, goal):
    idx1 = idx2 = 0
    isPossible = True
    
    for g in goal:
        if (idx1 < len(cards1)) and (cards1[idx1] == g):
            idx1+=1
        elif (idx2 < len(cards2)) and (cards2[idx2] == g):
            idx2+=1
        else:
            isPossible = False
            break
            
    if isPossible:
        answer = 'Yes'
    else:
        answer = 'No'
        
    return answer