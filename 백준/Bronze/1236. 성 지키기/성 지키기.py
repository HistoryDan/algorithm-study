import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[s for s in input().rstrip()] for _ in range(n)]
row = col = 0

# row count 
for i in range(n):
    if 'X'  not in graph[i]: row += 1

# columns count
for i in range(m):
    flag = True
    for j in range(n):
        if graph[j][i] == 'X':
            flag = False
            break
    if flag:
        col += 1

print(max(row, col))