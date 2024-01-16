import sys 

n, k = map(int, sys.stdin.readline().rstrip().split())
graph = [0 for _ in range(n)]
visited = [1] + [0 for _ in range(n-1)]
flag = True

for i in range(n):
    n = int(sys.stdin.readline().rstrip())
    graph[i] = n

cur = graph[0]
cnt = 1

while cur != k:
    if visited[cur]: 
        flag = False
        break
    visited[cur] = 1
    cur = graph[cur]
    cnt += 1

if flag:
    print(cnt)
else:
    print(-1)