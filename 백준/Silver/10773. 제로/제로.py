import sys

rep = int(sys.stdin.readline().rstrip())
stack = []

for _ in range(rep):
  num = int(sys.stdin.readline().rstrip())
  if num == 0:
    stack.pop()
  else:
    stack.append(num)

print(sum(stack))