import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
circles = []
smallest = 1010000
largest = -1010000

for _ in range(N):
    x, r = map(int, input().split())
    if (x-r) < smallest:
        smallest = (x-r)
    if (x+r) > largest:
        largest = (x+r)
    circles.append((x-r, x+r))


for i, circle in enumerate(circles):
    left, right = circle
    circles[i] = (left-smallest, right-smallest)

parentheses = [0]*(largest-smallest+1)

for i, circle in enumerate(circles):
    left, right = circle
    if parentheses[left] != 0 or parentheses[right] != 0:
        print('NO')
        sys.exit()
    else:
        parentheses[left] = (i,'l')
        parentheses[right] = (i,'r')

parentheses = [p for p in parentheses if p != 0]
stack = deque()

for idx, lr in parentheses:
    if lr == 'l':
        stack.append((idx, lr))
    else:
        if not stack:
            print('NO')
            sys.exit()
        else:
            if stack[-1][0] != idx or stack[-1][1] != 'l':
                print('NO')
                sys.exit()
            else:
                stack.pop()

if stack:
    print('NO')
else:
    print('YES')