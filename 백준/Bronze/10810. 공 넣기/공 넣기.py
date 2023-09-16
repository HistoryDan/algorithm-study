import sys

n, m = map(int, input().split())
numbers = [0 for i in range(n)]

for x in range(m):
  i,j,k = map(int, sys.stdin.readline().rstrip().split())
  numbers[i-1:j] = [k for y in range(i-1,j)]

print(*numbers)
