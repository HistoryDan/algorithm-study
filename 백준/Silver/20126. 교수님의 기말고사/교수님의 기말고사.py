import sys 

n,m,s = map(int, sys.stdin.readline().rstrip().split())
schedule = [(0,0)] + [0 for _ in range(n)]
flag = False

def key(x):
    return x[0]

for i in range(n):
    x,y = map(int, sys.stdin.readline().rstrip().split())
    schedule[i+1] = (x, x+y)

schedule.sort(key=key)
schedule += [(s,0)]
# print(schedule)

for i in range(n+1):
    if schedule[i+1][0] - schedule[i][1] >= m:
        flag = True
        answer = schedule[i][1]
        break

if flag:
    print(answer)
else:
    print(-1)