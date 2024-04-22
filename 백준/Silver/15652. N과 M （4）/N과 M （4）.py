import sys 
from itertools import combinations_with_replacement

N, M = map(int, input().split())
nums = [i for i in range(1,N+1)]
answers = []

for comb in combinations_with_replacement(nums, M):
    comb = sorted(list(comb))
    answers.append(comb)

for answer in answers:
    print(*answer)