import sys
from collections import deque 
input = sys.stdin.readline

N,M = map(int, input().split())
graph = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    graph.append(row)

visited = [[0]*M for _ in range(N)]
start_r = start_c = -1
for r in range(N):
    for c in range(M):
        if graph[r][c] == 2:
            start_r = r
            start_c = c
        elif graph[r][c] == 0:
            visited[r][c] = 1

dr = [1,-1,0,0]
dc = [0,0,1,-1]
queue = deque()
queue.append((start_r, start_c))
visited[start_r][start_c] = 1
while queue:
    r, c = queue.popleft()
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            graph[nr][nc] = graph[r][c] + 1
            queue.append((nr,nc))
            visited[nr][nc] = 1

for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            graph[r][c] = -1
        elif graph[r][c] >= 2:
            graph[r][c] -= 2

for i in range(N):
    print(*graph[i])