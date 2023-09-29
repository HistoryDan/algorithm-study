import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())

abc = sorted([a,b,c])
print(abc[1])