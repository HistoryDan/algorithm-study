import sys 
from collections import deque

# breadth first search
def bfs(graph,m,n):
    visited = [[0]*m for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    cnt = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1 and visited[j][i] == 0:
                cnt += 1
                queue = deque()
                queue.append((i,j))
                visited[j][i] = 1
                while queue:
                    x,y = queue.pop()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1 and visited[ny][nx] == 0:
                            queue.append((nx,ny))
                            visited[ny][nx] = 1
    return cnt

# main
t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().rstrip().split())
        graph[y][x] = 1
    print(bfs(graph, m, n))