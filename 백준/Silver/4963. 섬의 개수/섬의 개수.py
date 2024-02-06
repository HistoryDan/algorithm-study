import sys 
from collections import deque

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

def bfs(sx,sy):
    queue = deque()
    queue.append((sx,sy))
    graph[sy][sx] = 0
    while queue:
        x,y = queue.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < w and 0 <= ny < h and graph[ny][nx] == 1:
                queue.append((nx,ny))
                graph[ny][nx]=0

while True:
    graph = []
    w,h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0: break
    
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    
    cnt = 0
    for i in range(w):
        for j in range(h):
            if graph[j][i] == 1:
                bfs(i,j)
                cnt += 1
    print(cnt)