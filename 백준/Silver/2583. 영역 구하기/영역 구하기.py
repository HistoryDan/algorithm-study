import sys 
from collections import deque

# def print_graph(graph, m):
#     for i in range(m):
#         print(*graph[i])
#     print()

def bfs(sx,sy,m,n):
    global graph
    queue = deque()
    area = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue.append((sx,sy))
    graph[sy][sx] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 0:
                graph[ny][nx] = 1
                area += 1
                queue.append((nx,ny))

    return area

m,n,k = map(int, sys.stdin.readline().rstrip().split())
graph = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i] = 1
areas = []
cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            area = bfs(j,i,m,n)
            area += 1
            if area != 0: 
                areas.append(area)
                cnt += 1
print(cnt)
print(*sorted(areas))