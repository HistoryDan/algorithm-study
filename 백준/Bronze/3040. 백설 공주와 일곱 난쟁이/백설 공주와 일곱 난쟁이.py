import sys
import itertools

hobits = [0 for _ in range(9)]
for i in range(9):
    hobit = int(sys.stdin.readline().rstrip())
    hobits[i] = hobit

combs = itertools.combinations(hobits, 7)

for comb in combs:
    if sum(comb) == 100:
        # comb = sorted(comb)
        for c in comb:
            print(c)
        break
