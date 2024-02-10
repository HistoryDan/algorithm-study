import sys 
input = sys.stdin.readline

n = int(input().rstrip())
nums = [int(i) for i in input().rstrip().split()]
dp = [nums[0]]

# dp[i] := i번째 숫자를 마지막으로 하는 최대증가수열의 합
# dp[k] = (0번째부터 k-1번째 숫자 j들 중 N[j] < N[i]를 만족하고 dp[j]가 가장 큰 dp[j]) + N[k]

for i in range(1,n):
    temp = 0
    for j in range(i):
        if nums[i] > nums[j] and temp < dp[j]:
            temp = dp[j]
    dp.append(temp + nums[i])

print(max(dp))