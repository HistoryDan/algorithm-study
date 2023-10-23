import sys
hear = set()
see = set()
n, m = map(int, sys.stdin.readline().rstrip().split())

for _ in range(n):
    name = sys.stdin.readline().rstrip()
    hear.add(name)

for _ in range(m):
    name = sys.stdin.readline().rstrip()
    see.add(name)

rslt = hear.intersection(see)
rslt = sorted(rslt)

print(len(rslt))

for name in rslt:
    print(name)