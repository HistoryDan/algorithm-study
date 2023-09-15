import sys
lines = []

while True:
  line = sys.stdin.readline().rstrip()
  if line:
    lines.append(line)
  else:
    break

for line in lines:
  print(line)
  