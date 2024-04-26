import sys 
input = sys.stdin.readline

N,M = map(int, input().split())
nums = [0] + [int(i) for i in input().split()]
for i in range(1,len(nums)):
    nums[i] += nums[i-1]

cnt = 0
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[j] - nums[i] == M:
            cnt += 1
            break
        elif nums[j] - nums[i] > M:
            break

print(cnt)