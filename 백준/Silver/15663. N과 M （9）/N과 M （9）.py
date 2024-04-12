import sys
from itertools import permutations

N,M = map(int, input().split())
nums = [int(i) for i in input().split()]
answers = set()

for perm in permutations(nums, M):
    answers.add(perm)

answers = sorted(answers)
for answer in answers:
    print(*answer)