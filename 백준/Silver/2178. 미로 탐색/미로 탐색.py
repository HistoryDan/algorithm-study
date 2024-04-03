import sys 
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
graph = []
for _ in range(N):
    row = [int(i) for i in input().rstrip()]
    graph.append(row)

dr = [1,-1,0,0]
dc = [0,0,1,-1]
visited = [[0]*M for _ in range(N)]
queue = deque()
queue.append((0,0))

while queue:
    r,c = queue.popleft()
    visited[r][c] = 1
    for i in range(4):
        nr, nc = r + dr[i], c+dc[i]
        if 0 <= nr < N and 0 <= nc < M and graph[nr][nc] and not visited[nr][nc]:
            graph[nr][nc] = graph[r][c] + 1
            queue.append((nr,nc))
            visited[nr][nc] = 1

print(graph[N-1][M-1])