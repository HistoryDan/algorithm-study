import sys 
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
print(max(sum(a), sum(b)))