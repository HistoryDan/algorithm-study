import sys

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
  name = sys.stdin.readline().rstrip()
  alphabets = sys.stdin.readline().rstrip()
  rule = {}
  for i in range(26):
    rule[i+65] = alphabets[i]
  answer = ''
  for n in name:
    if ord(n) in rule:
      answer += rule[ord(n)]
    else:
      answer += n
  print(answer)