import sys

n = int(sys.stdin.readline().rstrip())
nums = sys.stdin.readline().rstrip()
nums = [int(num) for num in nums.split()]
nums1 = sorted(nums)
idx = 0
rslt = {nums1[0]:0}

for i in range(1, len(nums1)):
    if nums1[i] == nums1[i-1]:
        rslt[nums1[i]] = idx
    else:
        idx += 1
        rslt[nums1[i]] = idx

answer = []

for num in nums:
    answer.append(rslt[num])

print(*answer)
