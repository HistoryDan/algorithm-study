import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

parents = [0] * (N+1)
queue = deque()
queue.append(1)
visited = [0] * (N+1)
visited[1] = 1

while queue:
    cur = queue.pop()
    children = tree[cur]
    for child in children:
        if not visited[child]:
            visited[child] = 1
            parents[child] = cur
            queue.append(child)

parents = parents[2:]
for parent in parents:
    print(parent)