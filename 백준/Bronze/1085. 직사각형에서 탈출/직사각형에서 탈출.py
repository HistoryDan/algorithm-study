import sys

nums = list(map(int, sys.stdin.readline().split()))
answer = [nums[0], abs(nums[2]-nums[0]), nums[1], abs(nums[3]-nums[1])]

print(min(answer))