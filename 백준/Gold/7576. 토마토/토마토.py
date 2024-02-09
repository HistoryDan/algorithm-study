import sys 
from collections import deque

input = sys.stdin.readline

def not_ripen(graph, m, n):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return True
    return False

def get_max(graph, m, n):
    max = -2
    for i in range(n):
        for j in range(m):
            if graph[i][j] > max:
                max = graph[i][j]
    return max

m,n = map(int, input().split())
graph = [[int(i) for i in input().split()] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((j,i)) # x, y

# bfs
while queue:
    x,y = queue.popleft()
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
            graph[ny][nx] = graph[y][x] + 1
            queue.append((nx, ny))

if not_ripen(graph, m, n):
    print(-1)
elif get_max(graph, m, n) == 1:
    print(0)
else:
    print(get_max(graph, m, n)-1)