import sys
from collections import deque

while True:
    line = sys.stdin.readline().rstrip()
    stack = deque()
    answer = 'yes'

    if line == '.' : break
    for i in range(len(line)):
        if line[i] == '(' or line[i] == '[':
            stack.append(line[i])
        elif line[i] == ')':
            if stack:
                top = stack.pop()
                if top == '(' : continue
                else: 
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
        elif line[i] == ']':
            if stack:
                top = stack.pop()
                if top == '[' : continue
                else:
                    answer = 'no'
                    break
            else:
                answer = 'no'
                break
    if stack:
        answer = 'no'
    
    print(answer)
    

