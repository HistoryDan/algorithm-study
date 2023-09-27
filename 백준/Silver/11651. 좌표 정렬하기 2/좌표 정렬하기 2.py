import sys

rep = int(sys.stdin.readline().rstrip())
points = []

for _ in range(rep):
  x,y = map(int, sys.stdin.readline().rstrip().split())
  points.append((y,x))

points = sorted(points)
for y,x in points:
  print(x,y)
  