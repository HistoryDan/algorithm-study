import sys 
from itertools import permutations

N,M = map(int, input().split())
nums = [int(i) for i in input().split()]
answers = []

for permu in permutations(nums, M):
    answers.append(list(permu))

answers = sorted(answers)
for answer in answers:
    print(*answer)