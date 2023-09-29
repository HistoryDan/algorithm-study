import sys
rep = int(sys.stdin.readline().rstrip())


for _ in range(rep):
  answer = sys.stdin.readline().rstrip()
  score = 0
  stack = []
  for a in answer:
    if a == 'X':
      stack = []
      continue
    else:
      stack.append(a)
      score += len(stack)
  print(score)