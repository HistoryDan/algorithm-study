import sys 

key = sys.stdin.readline().rstrip()
enc = sys.stdin.readline().rstrip()
n = len(enc) // len(key) +1
m = len(key)
matrix = [[0 for _ in range(m)] for _ in range(n-1)]

for i in range(m):
    for j in range(n-1):
        matrix[j][i] = enc[i*(n-1)+j]
matrix = [[c for c in sorted(key)]] + matrix


answer = [[0 for _ in range(m)] for _ in range(n)]

idx = 0
for k in key:
    flag = True
    for i in range(m):
        if matrix[0][i] == k and flag and matrix[0][i] != 0:
            for j in range(n):
                answer[j][idx] = matrix[j][i]
            flag = False
            matrix[0][i] = 0
            idx += 1

for i in range(1,n):
    for j in range(m):
        print(answer[i][j], end = '')