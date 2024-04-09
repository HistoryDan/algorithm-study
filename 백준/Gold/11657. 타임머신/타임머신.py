import sys
input = sys.stdin.readline

N,M = map(int, input().split())
edges = []
for _ in range(M):
    A,B,C = map(int, input().split())
    edges.append((A,B,C))

table = ([float('inf')] * (N+1))
table[1] = 0
edges.sort()
flag = False
for i in range(N):
    for edge in edges:
        a,b,c = edge
        if table[a] != float('inf') and table[b] > table[a] + c:
            table[b] = table[a] + c 
            if i == N-1:
                flag = True

table = table[2:]
if flag:
    print(-1)
else:
    for dist in table:
        if dist == float('inf'):
            print(-1)
        else:
            print(dist)