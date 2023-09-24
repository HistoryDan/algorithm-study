import sys 

n = int(sys.stdin.readline().rstrip())
nums = [0 for _ in range(n)]

for i in range(n):
  num = int(sys.stdin.readline().rstrip())
  nums[i] = num

nums = sorted(nums)
for i in range(n):
  print(nums[i])