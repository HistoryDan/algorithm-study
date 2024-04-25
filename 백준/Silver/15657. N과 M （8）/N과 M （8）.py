import sys
from itertools import combinations_with_replacement

N,M = map(int, input().split())
nums = [int(i) for i in input().split()]
answer = []

for comb in combinations_with_replacement(nums, M):
    comb = list(sorted(comb))
    answer.append(comb)

answer = sorted(answer)
for a in answer:
    print(*a)