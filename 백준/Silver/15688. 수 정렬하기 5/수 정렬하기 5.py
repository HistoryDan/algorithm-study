import sys 
N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    num = int(sys.stdin.readline())
    nums.append(num)

for num in sorted(nums):
    print(num)