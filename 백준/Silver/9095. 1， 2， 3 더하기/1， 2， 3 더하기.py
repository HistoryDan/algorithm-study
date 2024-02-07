import sys

dp = [0,1,2,4] # n=1, n=2, n=3
for i in range(4,11):
    dp.append(dp[i-1]+dp[i-2]+dp[i-3])

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(dp[n])