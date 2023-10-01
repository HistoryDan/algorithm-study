import sys

def getgcd(n1, n2):
  large = max(n1, n2)
  small = min(n1, n2)
  mod = large % small
  while mod:
    large = small
    small = mod
    mod = large % small
  return small

rep = int(sys.stdin.readline().rstrip())
trees = [0 for _ in range(rep)]

for r in range(rep):
  trees[r] = int(sys.stdin.readline().rstrip())

diffs = []
gcd = 0

for r in range(1, rep):
  diff = trees[r] - trees[r-1]
  diffs.append(diff)

gcd = getgcd(diffs[0], diffs[1])

for d in range(2,len(diffs)):
  gcd = getgcd(gcd, diffs[d])
  
print((trees[-1] - trees[0]) // gcd - rep + 1)


  
  


