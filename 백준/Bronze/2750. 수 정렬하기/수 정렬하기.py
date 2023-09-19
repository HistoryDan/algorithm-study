import sys
iteration = int(input())
nums = []

for _ in range(iteration):
  num = sys.stdin.readline().rstrip()
  nums.append(int(num))

for i in range(len(nums)):
  for j in range(len(nums)-i-1):
    if nums[j] > nums[j+1]:
      temp = nums[j]
      nums[j] = nums[j+1]
      nums[j+1] = temp

for num in nums:
  print(num)