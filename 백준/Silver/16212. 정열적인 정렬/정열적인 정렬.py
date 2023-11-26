import sys
_ = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
nums = sorted(nums)
print(*nums)