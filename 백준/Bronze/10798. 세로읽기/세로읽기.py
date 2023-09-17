import sys
matrix = []
result = []
size = 0

for i in range(5):
  line = sys.stdin.readline().rstrip()
  if len(line) > size:
    size = len(line)
  matrix.append(line)

for i in range(5):
  if len(matrix[i]) < size:
    matrix[i] += ' '*(size-len(matrix[i]))

for i in range(size):
  for j in range(5):
    if matrix[j][i] == ' ':
      continue
    result.append(matrix[j][i])

print("".join(result))
  