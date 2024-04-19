import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = [int(i) for i in input().split()]
for i in range(N-1):
    nums[i+1] += nums[i]
nums = [0] + nums

for _ in range(M):
    i,j = map(int, input().split())
    print(nums[j] - nums[i-1])