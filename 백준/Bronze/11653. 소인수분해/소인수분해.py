n = int(input())
factors = []

for i in range(2, n+1):
  if n % i == 0:
    factors.append(i)

for factor in factors:
  if factor == 2 or factor % 2 != 0 :
    for i in range(2,factor):
      if factor % i == 0:
        factors.remove(factor)
        break

for factor in factors:
  while n % factor == 0:
    n //= factor
    print(factor)

