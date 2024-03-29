import sys
from itertools import combinations, permutations
input = sys.stdin.readline

N = int(input().rstrip())
members = {i for i in range(N)}
S = []
for _ in range(N):
    row = [int(i) for i in input().split()]
    S.append(row)

answer = float('inf')
for i in range(1, N//2+1):
    for comb in combinations(members, i):
        team1 = set(comb)
        team2 = members.difference(team1)
        stat1 = stat2 = 0
        if i != 1:
            for perm in permutations(team1, 2):
                a,b = perm
                stat1 += S[a][b]
        for perm in permutations(team2, 2):
            a,b = perm
            stat2 += S[a][b]
        diff = abs(stat1 - stat2)
        if diff < answer:
            answer = diff

print(answer)