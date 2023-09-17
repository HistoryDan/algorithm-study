import sys

iter = int(input())
black_matrix = [[0 for _ in range(100)] for _ in range(100)]

for k in range(iter):
  a,b = map(int, sys.stdin.readline().rstrip().split())
  for i in range(10):
    for j in range(10):
      black_matrix[99-b-i][a+j] = 1

total = 0
for i in range(100):
  total += sum(black_matrix[i])

print(total)
