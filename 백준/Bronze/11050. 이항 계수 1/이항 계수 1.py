import sys 

n, k = map(int, sys.stdin.readline().rstrip().split())

def factorial(x):
    fact = 1
    for i in range(1, x+1):
        fact *= i
    return fact

f1 = factorial(n)
f2 = factorial(k)
f3 = factorial(n-k)

print(int(f1/(f2*f3)))