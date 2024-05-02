import sys 
input = sys.stdin.readline

dp = [1, 2, 4]
for i in range(3, 1000001):
    new = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
    dp.append(new)

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n-1])