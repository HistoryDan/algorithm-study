import sys 
from itertools import permutations

n,m = map(int, sys.stdin.readline().rstrip().split())
nums = [i for i in range(1,n+1)]

for p in permutations(nums,m):
    print(*p)