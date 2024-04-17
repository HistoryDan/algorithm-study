import sys 
input = sys.stdin.readline

N,M = map(int, input().split())
graph = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    graph.append(row)

baby_sharks = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            baby_sharks.append((i,j)) # row, col

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            smallest_diff = float('inf')
            for baby_shark in baby_sharks:
                row, col = baby_shark
                row_diff = abs(i-row)
                col_diff = abs(j-col)
                row_col_diff = abs(row_diff - col_diff)
                min_diff = min(row_diff, col_diff)
                diff = row_col_diff + min_diff
                if smallest_diff > diff:
                    smallest_diff = diff
            graph[i][j] = smallest_diff

answer = -1
for i in range(N):
    for j in range(M):
        if graph[i][j] > answer:
            answer = graph[i][j]
print(answer)