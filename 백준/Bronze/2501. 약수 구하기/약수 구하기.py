a,b = map(int, input().split())
factors = []

for i in range(1,a+1):
  if a % i == 0:
    factors.append(i)

if b > len(factors):
  print('0')
else:
  print(factors[b-1])