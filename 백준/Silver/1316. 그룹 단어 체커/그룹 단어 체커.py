import sys
iter = int(input())
total = 0

for i in range(iter):
  word = sys.stdin.readline().rstrip()
  found = True
  if len(word) == 1:
    total += 1
    continue
  check = set()
  for j in range(len(word)-1):
    if (word[j+1] != word[j]) and (word[j+1] in check):
      found = False
      break
    else:
      check.add(word[j])

  if found:
    total += 1

print(total)
    