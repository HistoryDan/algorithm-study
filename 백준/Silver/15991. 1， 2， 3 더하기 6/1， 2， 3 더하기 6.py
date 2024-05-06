import sys 
input = sys.stdin.readline

dp = [1,2,2,3,3,6]
for i in range(6,100001):
    new = (dp[i-2] + dp[i-4] + dp[i-6]) % 1000000009
    dp.append(new)

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n-1])