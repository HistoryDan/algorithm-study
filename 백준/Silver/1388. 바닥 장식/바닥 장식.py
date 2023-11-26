import sys 
from collections import deque

cnt = 0
n,m = map(int, sys.stdin.readline().split())
floors = []
for _ in range(n):
    line = sys.stdin.readline().rstrip() + '|'
    floors.append(line)
last = '-' * m
floors.append(last)

for i in range(n):
    row = floors[i]
    stack = deque()
    for j in range(m+1):
        if row[j] == '-' : 
            stack.append(row[j])
        elif len(stack): 
            stack.clear()
            cnt += 1

for i in range(m):
    col = [floor[i] for floor in floors]
    stack = deque()
    for j in range(n+1):
        if col[j] == '|':
            stack.append(col[j])
        elif len(stack):
            stack.clear()
            cnt += 1

print(cnt)
