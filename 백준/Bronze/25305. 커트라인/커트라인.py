n,k = map(int, input().split())
nums = [int(i) for i in input().split()]

for i in range(len(nums)):
  for j in range(len(nums)-i-1):
    if nums[j] < nums[j+1]:
      temp = nums[j]
      nums[j] = nums[j+1]
      nums[j+1] = temp

print(nums[k-1])