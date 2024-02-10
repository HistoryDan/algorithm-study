import sys
input = sys.stdin.readline

# D[i] := N[i]로 끝나는 최장 증가 수열의 길이
# D[k] = max(D[j]) + 1 (0 <= j < k, N[j] < N[k])
n = int(input().rstrip())
nums = [int(i) for i in input().split()]
dp = [1]

for i in range(1,n):
    temp = 0
    for j in range(i):
        if nums[j] < nums[i] and dp[j] > temp:
            temp = dp[j]
    dp.append(temp+1)

print(max(dp))