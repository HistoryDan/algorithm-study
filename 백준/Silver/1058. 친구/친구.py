import sys
input = sys.stdin.readline

n = int(input().rstrip())
graph = [[1 if i=='Y' else 0 for i in input().rstrip()] for _ in range(n)]
ref = []

for i in range(n):
    adjs = set()
    friends = set()
    for j in range(n):
        if graph[i][j] == 1: 
            friends.add(j)
            adjs.add(j)
        for a in adjs:
            for k in range(n):
                if graph[a][k] == 1: friends.add(k)
    friends.discard(i)
    ref.append(len(friends))

ref.append(0)
print(max(ref))