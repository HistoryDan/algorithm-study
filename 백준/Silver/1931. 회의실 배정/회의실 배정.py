import sys 

n = int(sys.stdin.readline().rstrip())
schedule = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    schedule.append((start, end))

schedule.sort(key=lambda x : (x[1], x[0]))
cnt = 0
cur_end = 0

for s in schedule:
    if s[0] >= cur_end:
        cur_end = s[1]
        cnt += 1

print(cnt)