# D[i][0] := i번째 집을 빨간색으로 칠했을 때의 최소비용
# D[i][1] := i번째 집을 초록색으로 칠했을 때의 최소비용
# D[i][2] := i번째 집을 파란색으로 칠했을 때의 최소비용
# D[k][0] = min(D[k-1][1] + P[k][0], D[k-1][2] + P[k][0])
# D[k][1] = min(D[k-1][0] + P[k][1], D[k-1][2] + P[k][1])
# D[k][2] = min(D[k-1][0] + P[k][2], D[k-1][1] + P[k][2])

import sys 
input = sys.stdin.readline
n = int(input().rstrip())
prices = [[int(i) for i in input().rstrip().split()] for _ in range(n)]
dp = [prices[0]]

for i in range(1,n):
    red = min(dp[i-1][1]+prices[i][0], dp[i-1][2]+prices[i][0])
    green = min(dp[i-1][0]+prices[i][1], dp[i-1][2]+prices[i][1])
    blue = min(dp[i-1][0]+prices[i][2], dp[i-1][1]+prices[i][2])
    dp.append([red, green, blue])

print(min(dp[-1]))