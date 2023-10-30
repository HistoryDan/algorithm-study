import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
ss = sys.stdin.readline().rstrip()
ss = sorted([int(s) for s in ss.split()])
num = int(sys.stdin.readline().rstrip())
cnt = 0

if num not in ss:
    target = [i for i in range(1,1001)]
    for comb in combinations(target, 2):
        if num >= comb[0] and num <= comb[1]:
            check = True
            for s in ss:
                if s >= comb[0] and s <= comb[1]:
                    check = False
                    break
            if check:
                cnt += 1
print(cnt)