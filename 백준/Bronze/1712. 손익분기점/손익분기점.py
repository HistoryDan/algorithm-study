import sys

a,b,c = map(int, sys.stdin.readline().rstrip().split())
profit = c-b
if profit <= 0 :
    print(-1)
else:
    print(a//profit+1)