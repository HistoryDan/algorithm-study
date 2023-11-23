import sys
from itertools import combinations

def get_gcd(a, b):
    big = max(a,b)
    small = min(a,b)
    r = big % small
    while r != 0:
        big = small
        small = r
        r = big % small
    return small


n = int(sys.stdin.readline())

for _ in range(n):
    test = list(map(int, sys.stdin.readline().split()))
    test = test[1:]
    gcd_total = 0
    for comb in combinations(test, 2):
        gcd = get_gcd(comb[0], comb[1])
        gcd_total += gcd
    print(gcd_total)
