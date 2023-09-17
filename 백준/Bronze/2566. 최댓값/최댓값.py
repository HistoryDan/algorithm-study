import sys
matrix = []

for i in range(9):
  line = [int(i) for i in sys.stdin.readline().rstrip().split()]
  matrix.append(line)

largest = 0
row = 0
col = 0
for i in range(9):
  for j in range(9):
    if matrix[i][j] > largest:
      largest = matrix[i][j]
      row = i
      col = j
  
print(largest)
print(row+1, col+1)
