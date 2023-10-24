import sys
_,_ = map(int, sys.stdin.readline().rstrip().split())
a = sys.stdin.readline().rstrip()
a = set(a.split())
b = sys.stdin.readline().rstrip()
b = set(b.split())
c = a.intersection(b)
a = a-c
b = b-c
print(len(a) + len(b))