import sys
repeat = int(sys.stdin.readline().rstrip())

for _ in range(repeat):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  gcd = 1
  for i in range(1, min(a,b)+1):
    if a % i == 0 and b % i == 0:
      gcd = i

  lcm = gcd * (a // gcd) * (b // gcd)
  print(lcm)

