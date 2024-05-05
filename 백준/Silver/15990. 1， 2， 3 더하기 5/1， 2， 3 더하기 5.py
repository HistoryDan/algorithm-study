import sys 
input = sys.stdin.readline

dp = [(1,0,0), (0,1,0), (1,1,1)]

for i in range(3, 100001):
    ends_with_one = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    ends_with_two = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    ends_with_three = (dp[i-3][0] + dp[i-3][1]) % 1000000009
    dp.append((ends_with_one, ends_with_two, ends_with_three))

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(dp[n-1])%1000000009)