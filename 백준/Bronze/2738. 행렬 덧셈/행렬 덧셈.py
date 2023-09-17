import sys

n,m = map(int, input().split())
matrix1 = []
matrix2 = []

for i in range(n):
  line = [int(j) for j in sys.stdin.readline().rstrip().split()]
  matrix1.append(line)

for i in range(n):
  line = [int(j) for j in sys.stdin.readline().rstrip().split()]
  matrix2.append(line)

for i in range(n):
  for j in range(m):
    matrix1[i][j] += matrix2[i][j]
  print(*matrix1[i])

