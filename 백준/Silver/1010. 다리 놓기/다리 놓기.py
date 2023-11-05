import sys
from itertools import combinations

def factorial(x):
    rslt = 1
    for i in range(1, x+1):
        rslt *= i
    return rslt

rep = int(sys.stdin.readline().rstrip())

for _ in range(rep):
    m, n = map(int, sys.stdin.readline().rstrip().split())
    print(int(factorial(n) / (factorial(m) * factorial(n-m))))
