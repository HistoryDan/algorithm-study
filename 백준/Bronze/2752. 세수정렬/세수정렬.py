import sys 
nums = list(map(int, sys.stdin.readline().split()))
nums = sorted(nums)
print(*nums)