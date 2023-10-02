import sys

n = int(sys.stdin.readline().rstrip())
nums1 = [int(i) for i in sys.stdin.readline().rstrip().split()]

m = int(sys.stdin.readline().rstrip())
nums2 = [int(i) for i in sys.stdin.readline().rstrip().split()]

nums1 = set(nums1)

for num in nums2:
  if num in nums1:
    print(1)
  else:
    print(0)
  