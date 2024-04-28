import sys 
from collections import deque
input = sys.stdin.readline

N = int(input())
is_good = True
cnt = 0
for _ in range(N):
    string = input().rstrip()
    stack = deque()
    for s in string:
        if not stack:
            stack.append(s)
        else:
            if s == 'A':
                if stack[-1] == 'A':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == 'B': 
                if stack[-1] == 'B':
                    stack.pop()
                else:
                    stack.append(s)
    if not stack:
        cnt += 1

print(cnt)