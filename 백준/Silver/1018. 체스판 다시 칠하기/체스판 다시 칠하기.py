import sys

m,n = map(int, input().split())
matrix = []
line_w = ['W' if i % 2 == 0 else 'B' for i in range(8)]
line_b = ['B' if i % 2 == 0 else 'W' for i in range(8)]
answer_w = [line_w if i % 2 == 0 else line_b for i in range(8)]
answer_b = [line_b if i % 2 == 0 else line_w for i in range(8)]

for i in range(m):
  line = sys.stdin.readline().rstrip()
  matrix.append(list(line))

smallest = 64
for i in range(m-8+1):
  for j in range(n-8+1):
    count_w = 0
    count_b = 0
    for k in range(8):
      for p in range(8):
        if matrix[i+k][j+p] != answer_w[k][p]:
          count_w += 1
        if matrix[i+k][j+p] != answer_b[k][p]:
          count_b += 1
    temp = min(count_w, count_b)
    if temp < smallest:
      smallest = temp

print(smallest)