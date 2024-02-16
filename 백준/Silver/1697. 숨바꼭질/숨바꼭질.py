import sys 
from collections import deque

n, k = map(int, sys.stdin.readline().split())
graph = [-1] * 100001
graph[n] = 0
queue = deque([n])

if n == k:
    print(0)
    sys.exit()

while queue:
    cur = queue.popleft()
    for next in [cur -1, cur + 1, cur * 2]:
        if next == k:
            print(graph[cur] + 1)
            sys.exit()
        if 0 <= next < len(graph) and graph[next] == -1:
            graph[next] = graph[cur] + 1
            queue.append(next)