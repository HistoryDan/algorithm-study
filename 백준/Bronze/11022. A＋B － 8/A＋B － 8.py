import sys

iter = int(input())

for i in range(iter):
  a,b = map(int, sys.stdin.readline().rstrip().split())
  print("Case #" + str(i+1) + ":", a, "+", b, "=", a + b)