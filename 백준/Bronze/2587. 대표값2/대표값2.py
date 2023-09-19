import sys
nums = []

for _ in range(5):
  num = sys.stdin.readline().rstrip()
  nums.append(int(num))

for i in range(len(nums)):
  for j in range(len(nums)-i-1):
    if nums[j] > nums[j+1]:
      temp = nums[j]
      nums[j] = nums[j+1]
      nums[j+1] = temp

print(sum(nums)//5)
print(nums[2])