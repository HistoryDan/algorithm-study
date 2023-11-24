import sys 

string = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
cnt = 0
for _ in range(n):
    line = sys.stdin.readline().rstrip()
    line = line * 3
    if string in line: cnt+=1
print(cnt)