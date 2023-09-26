import sys

rep = int(sys.stdin.readline().rstrip())
points = []

for _ in range(rep):
  x,y = map(int, sys.stdin.readline().rstrip().split())
  points.append([x,y])

points.sort()
  
for point in points:
  print(*point)




