import sys 
from collections import deque
input = sys.stdin.readline

def bfs(sx, sy):
    allies = []
    total = 0
    queue = deque()
    visited[sy][sx] = 1
    queue.append((sx, sy))
    while queue:
        x, y = queue.popleft()
        allies.append((x,y))
        total += graph[y][x]
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<N and 0<=ny<N and L <= abs(graph[y][x]-graph[ny][nx]) <= R and visited[ny][nx] == 0:
                visited[ny][nx]=1
                queue.append((nx,ny))

    return allies, total

# setting
N, L, R = map(int, input().rstrip().split())
graph = [[int(i) for i in input().rstrip().split()] for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
cnt = 0

while True:
    flag = True
    # breadth first search
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[j][i] == 0:
                allies, total = bfs(i,j)
                if len(allies) > 1:
                    flag = False
                    new = int(total/len(allies))
                    for ally in allies:
                        x,y = ally
                        graph[y][x] = new
    if flag:
        break
    # increment cnt
    cnt += 1

# answer
print(cnt)