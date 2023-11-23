import sys 
n = int(sys.stdin.readline())

nums = [0 for _ in range(n)]
for i in range(n):
    num = int(sys.stdin.readline())
    nums[i] = num
nums = sorted(nums, reverse = True)

for num in nums:
    print(num)