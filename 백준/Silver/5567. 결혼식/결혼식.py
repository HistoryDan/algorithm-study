import sys 

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
graph = [0] + [set() for _ in range(n)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].add(b)
    graph[b].add(a)

# print(graph)
ref = [1] + list(graph[1])
answer = set()
for r in ref:
    for i in graph[r]:
        if i != 1:
            answer.add(i)

print(len(answer))