import sys
n = int(sys.stdin.readline().rstrip())
rslt = set()

for _ in range(n):
    line = sys.stdin.readline().rstrip()
    e_or_l = line[-5:]
    name = line[:-6]
    if e_or_l == 'enter':
        rslt.add(name)
    else:
        rslt.remove(name)
rslt = sorted(rslt)
rslt.reverse()

for name in rslt:
    print(name)