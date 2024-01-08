import sys 

n,m = map(int, sys.stdin.readline().rstrip().split())
numerator = 1
denominator = 1

for i in range(n,(n-m),-1):
    numerator *= i
    denominator *= (n - i +1)

print(numerator // denominator)