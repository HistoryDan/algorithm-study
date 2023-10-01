import sys

def gcd(n1, n2):
  large = max(n1, n2)
  small = min(n1, n2)
  mod = large % small
  while mod:
    large = small
    small = mod
    mod = large % small
  return small

a, b = map(int, sys.stdin.readline().rstrip().split())
c, d = map(int, sys.stdin.readline().rstrip().split())

down = b * d
up = a*d + b*c

div = gcd(up, down)

print(up//div, down//div)


