import math
from collections import deque

def solution(progresses, speeds):
    days = [math.ceil((100 - progresses[i]) / speeds[i]) for i in range(len(speeds))]
    answer = []
    
    stack = deque()
    stack.append(days[0])
    largest = days[0]
    
    for i in range(1, len(days)):
        cur = days[i]
        if cur <= largest:
            stack.append(cur)
        else:
            largest = cur
            answer.append(len(stack))
            stack.clear()
            stack.append(largest)
    if stack:
        answer.append(len(stack))
    return answer