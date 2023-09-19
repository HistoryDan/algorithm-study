import sys

while True:
  n = int(sys.stdin.readline().rstrip())
  if n == -1:
    break
  factors = []
  for i in range(1,n):
    if n % i == 0:
      factors.append(i)
  if sum(factors) == n :
    factors = map(str, factors)
    print(str(n) + ' = ' + ' + '.join(factors))
  else:
    print(str(n), 'is NOT perfect.')
