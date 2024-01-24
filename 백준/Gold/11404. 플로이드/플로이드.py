import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c
    
for i in range(n):
    for j in range(n):
        if i == j : graph[i][j] = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][k] > graph[j][i] + graph[i][k]:
                graph[j][k] = graph[j][i] + graph[i][k]

for i in range(n):
    for j in range(n):
        if graph[i][j] == sys.maxsize : graph[i][j] = 0

for i in range(n):
    print(*graph[i])

