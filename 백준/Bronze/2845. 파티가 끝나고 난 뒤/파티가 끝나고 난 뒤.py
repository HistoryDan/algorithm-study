import sys

n,p = map(int, sys.stdin.readline().rstrip().split())
nums = sys.stdin.readline().rstrip().split()

ppl = n * p
answer = []
for num in nums:
  answer.append(int(num) - ppl)

print(*answer)