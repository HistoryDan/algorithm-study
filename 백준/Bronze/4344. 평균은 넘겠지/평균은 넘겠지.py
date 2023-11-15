import sys
n = int(sys.stdin.readline())
for _ in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    line = line[1:]
    avg = sum(line) / len(line)
    cnt = 0
    for score in line:
        if score > avg: cnt+=1
    print('{0:0.3f}%'.format(cnt/len(line)*100))




