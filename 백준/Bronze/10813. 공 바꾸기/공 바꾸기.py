import sys

n, m = map(int, input().split())
numbers = [i for i in range(1,n+1)]

for x in range(m):
  i,j = map(int, sys.stdin.readline().rstrip().split())
  temp = numbers[i-1]
  numbers[i-1] = numbers[j-1]
  numbers[j-1] = temp

print(*numbers)
