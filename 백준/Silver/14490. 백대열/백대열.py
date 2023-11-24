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

n,m = map(int, sys.stdin.readline().split(':'))
gcd = get_gcd(n,m)

print(str(n//gcd)+':'+str(m//gcd))