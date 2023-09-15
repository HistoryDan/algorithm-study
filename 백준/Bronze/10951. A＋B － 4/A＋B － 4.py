import sys
numbers = []

while True:
  line = sys.stdin.readline().rstrip()
  if line:
    a,b = map(int, line.split())
    numbers.append((a,b))
  else: 
    break

for i in range(len(numbers)):
  print(numbers[i][0] + numbers[i][1])