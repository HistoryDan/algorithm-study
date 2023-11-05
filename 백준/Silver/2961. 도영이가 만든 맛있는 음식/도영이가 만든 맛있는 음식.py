from itertools import combinations
import sys
n = int(sys.stdin.readline().rstrip())
ing = [0 for _ in range(n)]

for i in range(n):
    s, b = map(int, sys.stdin.readline().rstrip().split())
    ing[i] = (s, b)

diff = abs(s-b)

for i in range(1,n+1):
    for comb in combinations(ing, i):
        sour = 1
        bitter = 0
        for c in comb:
            sour *= c[0]
            bitter += c[1]
    
        temp_diff = abs(sour - bitter)

        if temp_diff < diff:
            diff = temp_diff

print(diff)

