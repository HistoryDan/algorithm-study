import sys 
from collections import deque

graph = []
r,c = map(int, sys.stdin.readline().rstrip().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(r):
    row = [0 if s== '.' else 1 for s in sys.stdin.readline().rstrip()]
    graph.append(row)

graph_n = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        graph_n[i][j] = graph[i][j]

for i in range(r):
    for j in range(c):
        x,y = j,i
        if graph[y][x] == 1:
            cnt = 0
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] == 0:
                    cnt += 1
                elif nx < 0 or nx >= c or ny < 0 or ny >= r:
                    cnt += 1
            if cnt >= 3:
                graph_n[y][x] = 0
# print(graph_n)

top = bottom = left= right = 0
# top 
for i in range(r):
    if 1 in graph_n[i]:
        top = i
        break
# bottom
for i in range(r-1,-1,-1):
    if 1 in graph_n[i]:
        bottom = i
        break
# right
for i in range(c):
    for j in range(r):
        if graph_n[j][i] == 1:
            right = i
            break
# left
for i in range(c-1,-1,-1):
    for j in range(r):
        if graph_n[j][i] == 1:
            left = i
            break       

for i in range(r):
    for j in range(c):
        if graph_n[i][j] == 1:
            graph_n[i][j] = 'X'
        else:
            graph_n[i][j] = '.'

# print(top, bottom, left, right)
graph_n = graph_n[top:bottom+1]
for line in graph_n:
    print(''.join(line[left:right+1]))