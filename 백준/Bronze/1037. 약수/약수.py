import sys

n = int(sys.stdin.readline())
divisors = list(map(int, sys.stdin.readline().split()))
result = 1

if len(divisors) % 2 == 0:
    divisors = sorted(divisors)
    result = min(divisors) * max(divisors)

else:
    divisors = sorted(divisors)
    div = divisors[(len(divisors)//2)]
    result = div ** 2

print(result)