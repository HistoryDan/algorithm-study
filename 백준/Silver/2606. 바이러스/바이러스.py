import sys 

node = int(sys.stdin.readline().rstrip())
edge = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(node+1)]
visited = [0] * (node + 1)

# graph initialization
for i in range(edge):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a] += [b]
    graph[b] += [a]

def dfs(v):
    visited[v] = 1
    for adj in graph[v]:
        if not visited[adj]:
            dfs(adj)

dfs(1)
print(sum(visited)-1)