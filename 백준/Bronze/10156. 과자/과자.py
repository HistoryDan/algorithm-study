import sys 
k,n,m = map(int, sys.stdin.readline().split())
answer = k*n-m
if answer < 0 : answer = 0
print(answer)