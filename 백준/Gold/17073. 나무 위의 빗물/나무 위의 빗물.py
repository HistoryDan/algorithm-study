# simply calculate the number of leaf nodes

import sys
input = sys.stdin.readline

N, W = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)


num_leaves = 0
for i in range(2,N+1): # except root node
    if len(graph[i]) == 1:
        num_leaves += 1

print(W / num_leaves)