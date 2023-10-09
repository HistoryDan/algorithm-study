import sys

n,p = map(int, sys.stdin.readline().rstrip().split())
print((p - 1) * n + 1)