import sys 
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[b].append(a)

# bfs
counts = [0 for _ in range(n+1)]
for i in range(1,n+1):
    cnt = 0
    queue = deque()
    visited = [0] * (n+1)
    visited[i] = 1
    queue.append(i)
    while queue:
        cur = queue.popleft()
        cnt += 1
        for adj in graph[cur]:
            if visited[adj] == 0:
                visited[adj]=1
                queue.append(adj)
    counts[i] = cnt

# output
maximum = max(counts)
for i in range(1,n+1):
    if counts[i] == maximum:
        print(i, end=' ')