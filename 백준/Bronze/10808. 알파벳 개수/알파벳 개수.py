import sys

word = sys.stdin.readline().rstrip()
rslt = []
for i in range(97,123):
    count = word.count(chr(i))
    rslt.append(count)


print(' '.join([str(r) for r in rslt]))

