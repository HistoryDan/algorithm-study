import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    row = [c for c in input().rstrip()]
    graph.append(row)

blind = not_blind = 0
visited = [[0] * N for _ in range(N)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

# not blind
for r in range(N):
    for c in range(N):
        if visited[r][c]:
            continue
        cur = graph[r][c]
        queue = deque()
        queue.append((r,c))
        visited[r][c] = 1
        while queue:
            cr, cc = queue.popleft()
            for i in range(4):
                nr, nc = cr + dr[i], cc + dc[i]
                if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] == cur and not visited[nr][nc]:
                    queue.append((nr,nc))
                    visited[nr][nc] = 1
        not_blind += 1

visited = [[0] * N for _ in range(N)]
# blind
for r in range(N):
    for c in range(N):
        if visited[r][c]:
            continue
        cur = graph[r][c]
        queue = deque()
        queue.append((r,c))
        visited[r][c] = 1
        if cur == 'R' or cur == 'G':
            while queue:
                cr, cc = queue.popleft()
                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and (graph[nr][nc] == 'R' or graph[nr][nc] == 'G'):
                        queue.append((nr,nc))
                        visited[nr][nc] = 1
        else:
            while queue:
                cr, cc = queue.popleft()
                for i in range(4):
                    nr, nc = cr + dr[i], cc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and graph[nr][nc] == cur:
                        queue.append((nr,nc))
                        visited[nr][nc] = 1
        blind += 1

print(not_blind, blind)