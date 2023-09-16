import sys

iter = int(input())
for i in range(iter):
  result = []
  num, string = sys.stdin.readline().rstrip().split()
  for j in range(len(string)):
    result.append(string[j] * int(num))
  print(''.join(result))
  