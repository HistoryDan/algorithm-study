import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
skylines = []
for _ in range(N):
    x,y = map(int, input().split())
    skylines.append((x,y))

skylines.sort(key= lambda x: x[0])
stack = deque()
cnt = 0
for _, h in skylines:
    if h == 0:
        stack.clear()
        continue
    if not stack:
        stack.append(h)
        cnt += 1
    else:
        top = stack[-1]
        if top < h:
            stack.append(h)
            cnt += 1
        else:
            while stack and stack[-1] > h:
                stack.pop()
            if stack and stack[-1] == h:
                pass
            else:
                stack.append(h)
                cnt += 1

print(cnt)