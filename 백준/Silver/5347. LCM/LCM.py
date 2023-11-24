import sys

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
    a,b = map(int, sys.stdin.readline().split())
    gcd = get_gcd(a,b)
    print(gcd * (a//gcd) * (b//gcd))
