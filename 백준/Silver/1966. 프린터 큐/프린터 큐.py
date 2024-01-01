import sys
from collections import deque

rep = int(sys.stdin.readline().rstrip())

for _ in range(rep):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    priorities = sys.stdin.readline().rstrip().split()
    queue = deque()
    
    for i,p in enumerate(priorities):
        queue.append((i,int(p)))

    cnt = 0
    while True:
        current = queue.popleft()
        poped = (999,999)
        state = True
        for q in queue:
            if q[1] > current[1]:
                queue.append(current)
                state = False
                break
        
        if state: 
            poped = current
            cnt += 1
        
        if poped[0] == m:
            break

    print(cnt)

