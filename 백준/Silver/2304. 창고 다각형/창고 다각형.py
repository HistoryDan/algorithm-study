import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
cols = []
largest_h = -1
for _ in range(N):
    L, H = map(int, input().split())
    if H > largest_h:
        largest_h = H
    cols.append((L, H))

cols.sort(key = lambda x: x[0])

mid1 = mid2 = -1
for i in range(N):
    if cols[i][1] == largest_h:
        mid1 = i
        break

for i in range(N-1,-1,-1):
    if cols[i][1] == largest_h:
        mid2 = i
        break

if mid1 == mid2:
    front = cols[:mid1+1]
    back = cols[mid1:][::-1]
else:
    front = cols[:mid1+1]
    back = cols[mid2:][::-1]

stack1 = deque()
stack2 = deque()

front_area = 0
back_area = 0

# front
for f in front:
    if not stack1:
        stack1.append(f)
    else:
        if stack1[-1][1] < f[1]:
            front_area += (stack1[-1][1]) * (f[0] - stack1[-1][0])
            stack1.pop()
            stack1.append(f)
    
# back
for b in back:
    if not stack2:
        stack2.append(b)
    else:
        if stack2[-1][1] < b[1]:
            back_area += (stack2[-1][1]) * (stack2[-1][0] - b[0])
            stack2.pop()
            stack2.append(b)

print(front_area + back_area + largest_h * (cols[mid2][0]-cols[mid1][0]+1))