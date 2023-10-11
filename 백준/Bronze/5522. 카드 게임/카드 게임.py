import sys
nums = []
for i in range(5):
    num = int(sys.stdin.readline().rstrip())
    nums.append(num)

print(sum(nums))