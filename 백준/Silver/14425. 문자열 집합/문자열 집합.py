import sys

n, m = map(int, input().split())
s = set()
cnt = 0

for _ in range(n):
  string = sys.stdin.readline().rstrip()
  s.add(string)

for _ in range(m):
  string = sys.stdin.readline().rstrip()
  if string in s: 
    cnt += 1

print(cnt)