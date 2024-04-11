import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    u,v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

answer = 0
visited = [0] * N
for i in range(N):
    if visited[i]:
        continue
    queue = deque()
    queue.append(i)
    visited[i]=1
    while queue:
        adjs = graph[queue.popleft()]
        for adj in adjs:
            if not visited[adj]:
                queue.append(adj)
                visited[adj] = 1
    answer += 1

print(answer)