import sys 

a,b = map(int, sys.stdin.readline().split())
c,d = map(int, sys.stdin.readline().split())
answer = min(a+d, b+c)
print(answer)