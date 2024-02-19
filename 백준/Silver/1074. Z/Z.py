import sys 

n,r,c = map(int, input().split())

def z(n, x, y):
    if n == 0:
        return 0
    half = 1 << (n - 1)
    if x < half and y < half:
        return z(n - 1, x, y)
    if x < half and y >= half:
        return half * half + z(n - 1, x, y - half)
    if x >= half and y < half:
        return 2 * half * half + z(n - 1, x - half, y)
    return 3 * half * half + z(n - 1, x - half, y - half)

print(z(n, r, c))