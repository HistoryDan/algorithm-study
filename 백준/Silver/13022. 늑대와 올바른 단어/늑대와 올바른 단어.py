import sys
from collections import deque

string = input().rstrip()
stack = deque()

for s in string:
    if s == 'w':
        if not stack:
            stack.append(['w',0])
        elif stack[-1][0] == 'w':
            stack[-1][1] += 1
        elif stack[-1][0] == 'f' and len(stack) == 4:
            if stack.pop()[1] == stack.pop()[1] == stack.pop()[1] == stack.pop()[1]:
                stack.append(['w',0])
            else:
                print(0)
                sys.exit()
        else:
            print(0)
            sys.exit()
        
    elif s == 'o':
        if stack and stack[-1][0] == 'w':
            stack.append(['o',0])
        elif stack and stack[-1][0] == 'o':
            stack[-1][1] += 1
        else:
            print(0)
            sys.exit()
        
    elif s == 'l':
        if stack and stack[-1][0] == 'o':
            stack.append(['l',0])
        elif stack and stack[-1][0] == 'l':
            stack[-1][1] += 1
        else:
            print(0)
            sys.exit()

    elif s == 'f':
        if stack and stack[-1][0] == 'l':
            stack.append(['f', 0])
        elif stack and stack[-1][0] == 'f':
            stack[-1][1] += 1
        else:
            print(0)
            sys.exit()  

if len(stack) == 4 and stack.pop()[1] == stack.pop()[1] == stack.pop()[1] == stack.pop()[1]:
    print(1)
else:
    print(0)
