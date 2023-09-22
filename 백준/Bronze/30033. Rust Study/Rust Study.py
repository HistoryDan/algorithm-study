import sys

n = int(sys.stdin.readline().rstrip())
sch = [int(i) for i in sys.stdin.readline().rstrip().split()]
real = [int(i) for i in sys.stdin.readline().rstrip().split()]
cnt = 0

for i in range(n):
  if sch[i] <= real[i]:
    cnt += 1

print(cnt)