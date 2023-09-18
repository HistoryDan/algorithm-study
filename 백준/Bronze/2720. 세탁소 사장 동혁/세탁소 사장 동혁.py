import sys

iter = int(input())
coins = [25, 10, 5, 1]

for i in range(iter):
  counts = [0,0,0,0]
  num = int(sys.stdin.readline().rstrip())
  for j in range(4):
    counts[j] = num // coins[j]
    num = num % coins[j]
  print(*counts)