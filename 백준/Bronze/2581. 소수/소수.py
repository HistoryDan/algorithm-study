m = int(input())
n = int(input())
primes = []

for i in range(m, n+1):
  if i == 1:
    continue
  cnt = 0
  for j in range(2, i-1):
    if i % j == 0:
      cnt += 1
      break
  if cnt == 0:
    primes.append(i)

if len(primes) == 0:
  print(-1)

else:
  print(sum(primes))
  print(primes[0])