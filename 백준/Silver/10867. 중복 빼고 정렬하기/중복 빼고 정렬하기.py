import sys 
n = int(sys.stdin.readline())
nums = list(set(map(int, sys.stdin.readline().split())))
nums = sorted(nums)
print(*nums)