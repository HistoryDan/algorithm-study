import sys 
from collections import deque
input = sys.stdin.readline

N,P = map(int, input().split())
stack1, stack2, stack3, stack4, stack5, stack6 = deque(), deque(), deque(), deque(), deque(), deque()
cnt = 0
for _ in range(N):
    string, prat = map(int, input().split())
    if string == 1:
        while stack1 and stack1[-1] > prat:
            stack1.pop()
            cnt += 1
        if stack1 and prat == stack1[-1]:
            continue
        stack1.append(prat)
        cnt += 1

    elif string == 2:
        while stack2 and stack2[-1] > prat:
            stack2.pop()
            cnt +=1
        if stack2 and prat == stack2[-1]:
            continue
        stack2.append(prat)
        cnt += 1

    elif string == 3:
        while stack3 and stack3[-1] > prat:
            stack3.pop()
            cnt +=1
        if stack3 and prat == stack3[-1]:
            continue
        stack3.append(prat)
        cnt += 1

    elif string == 4:
        while stack4 and stack4[-1] > prat:
            stack4.pop()
            cnt +=1
        if stack4 and prat == stack4[-1]:
            continue 
        stack4.append(prat)
        cnt += 1

    elif string == 5:
        while stack5 and stack5[-1] > prat:
            stack5.pop()
            cnt +=1
        if stack5 and prat == stack5[-1]:
            continue        
        stack5.append(prat)
        cnt += 1

    elif string == 6:
        while stack6 and stack6[-1] > prat:
            stack6.pop()
            cnt +=1
        if stack6 and prat == stack6[-1]:
            continue        
        stack6.append(prat)
        cnt += 1

print(cnt)