import sys 

def cnt(n,k):
    ret = 0
    while n > 0:
        n -= k
        ret += 1
    return ret

n,k = map(int, sys.stdin.readline().rstrip().split())
boys = [0 for _ in range(6)]
girls = [0 for _ in range(6)]

for _ in range(n):
    s,y = map(int, sys.stdin.readline().rstrip().split())
    if s == 1:
        boys[y-1] += 1
    else:
        girls[y-1] += 1

answer = 0
 
for i in range(6):
    answer += cnt(boys[i], k)
    answer += cnt(girls[i], k)

print(answer)
