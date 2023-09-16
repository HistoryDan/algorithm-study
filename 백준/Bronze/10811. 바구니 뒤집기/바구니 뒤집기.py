import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = [i+1 for i in range(n)]

for i in range(m):
  i, j = map(int, sys.stdin.readline().rstrip().split())
  numbers[i-1:j] = [numbers[idx] for idx in range(j-1,i-2, -1)]
  
print(*numbers)