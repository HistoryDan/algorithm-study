import sys
n = int(sys.stdin.readline().rstrip())
names = {}
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if len(name) in names:
        names[len(name)].add(name)
    else:
        names[len(name)] = set()
        names[len(name)].add(name)

rslt = []
keys = list(names.keys())
keys = sorted(keys)

for key in keys:
    rslt.extend(sorted(names[key]))

for r in rslt:
    print(r)