import sys
n = int(sys.stdin.readline().rstrip())
numbers = sys.stdin.readline().rstrip()
total = 0

for i in range(n):
  total += int(numbers[i])

print(total)