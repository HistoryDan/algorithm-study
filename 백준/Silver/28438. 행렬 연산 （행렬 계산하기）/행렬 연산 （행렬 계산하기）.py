import sys 

n,m,q = map(int, sys.stdin.readline().rstrip().split())
matrix = [[[0,0] for _ in range(m)] for _ in range(n)]
for _ in range(q):
    c,r,v = map(int, sys.stdin.readline().rstrip().split())
    if c==1:
        matrix[r-1][0][0] += v
    else:
        matrix[0][r-1][1] += v

for i in range(m):
    elem = matrix[0][i][1]
    for j in range(n):
        matrix[j][i][1] = elem

for i in range(n):
    elem = matrix[i][0][0]
    for j in range(m):
        matrix[i][j][0] = elem

answer = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        answer[i][j] = sum(matrix[i][j])
        
for i in range(n):
    print(*answer[i])
