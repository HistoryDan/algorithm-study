import sys 
from itertools import combinations

n,k = map(int, sys.stdin.readline().rstrip().split())
ab = bc = ca = 0
comp = []
for _ in range(n):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    comp.append((a+b,b+c,c+a))

comp1 = sorted(comp, key=lambda x : x[0], reverse=True)
comp2 = sorted(comp, key=lambda x : x[1], reverse=True)
comp3 = sorted(comp, key=lambda x : x[2], reverse=True)

for i in range(k):
    ab += comp1[i][0]

for i in range(k):
    bc += comp2[i][1]

for i in range(k):
    ca += comp3[i][2]

print(max(ab, bc, ca))

