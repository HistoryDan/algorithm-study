import sys
input = sys.stdin.readline

dp = [[0]*10 for _ in range(101)]
for i in range(1,10):
    dp[1][i] = 1

for i in range(2,len(dp)):
    dp[i][0] = dp[i-1][1]
    for j in range(1,9):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1])
    dp[i][9] = dp[i-1][8]

N = int(input())
print(sum(dp[N])%1000000000)