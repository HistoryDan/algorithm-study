import sys

stars = int(sys.stdin.readline().rstrip())
for s in range(stars,0,-1):
  print('*'*s)