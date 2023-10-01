import sys

a, b = map(int, sys.stdin.readline().rstrip().split())
large = max(a,b)
small = min(a,b)
mod = large % small

while mod:
  large = small
  small = mod
  mod = large % small

gcd = small

print(gcd * (a // gcd) * (b // gcd))
