import sys 
from collections import deque
input = sys.stdin.readline

# setting
n = int(input().rstrip())
graph = [[int(i) for i in input().rstrip()] for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
areas = []

# search
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            # bfs
            area = 0
            queue = deque()
            graph[i][j] = 0
            queue.append((j,i))
            while queue:
                x,y = queue.popleft()
                area += 1
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n and graph[ny][nx] == 1:
                        graph[ny][nx] = 0
                        queue.append((nx, ny))
            areas.append(area)

# output
areas.sort()
print(len(areas))
for area in areas:
    print(area)