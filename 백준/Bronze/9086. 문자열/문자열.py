import sys

iter = int(input())
for i in range(iter):
  string = sys.stdin.readline().rstrip()
  print(string[0]+string[-1])