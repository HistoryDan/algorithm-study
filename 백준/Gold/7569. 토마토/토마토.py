import sys
from collections import deque

m,n,h = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(h):
    mat = []
    for _ in range(n):
        row = [int(i) for i in sys.stdin.readline().rstrip().split()]
        mat.append(row)
    graph.append(mat)

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
queue = deque()

def bfs():
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0<= nz < h and graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                queue.append((nz, ny, nx))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i,j,k))
bfs()

flag = True
biggest = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            cur = graph[i][j][k]
            if cur == 0 :
                flag = False
                break
            if cur > biggest:
                biggest = cur

if flag:
    if biggest == 1:
        print(0)
    else:
        print(biggest-1)
else:
    print(-1)