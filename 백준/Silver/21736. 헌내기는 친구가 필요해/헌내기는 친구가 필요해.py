import sys 
from collections import deque

n,m = map(int, sys.stdin.readline().rstrip().split())
graph = [[s for s in sys.stdin.readline().rstrip()] for _ in range(n)]
ix = iy = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# find starting index
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            ix, iy = j, i
            break

# bfs
cnt = 0
queue = deque()
queue.append((ix, iy))
graph[iy][ix] = 'X'
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] != 'X':
            if graph[ny][nx] == 'P' : cnt += 1
            queue.append((nx, ny))
            graph[ny][nx] = 'X'

# answer
if cnt:
    print(cnt)
else:
    print('TT')