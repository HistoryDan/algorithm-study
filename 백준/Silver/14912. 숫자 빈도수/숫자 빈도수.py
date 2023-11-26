import sys
n,d = map(int, sys.stdin.readline().split())
d = str(d)
cnt = 0
for i in range(1,n+1):
    num = str(i)
    cnt += num.count(d)
print(cnt)