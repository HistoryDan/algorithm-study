import sys 
input = sys.stdin.readline

import sys
input = sys.stdin.readline

dp = [[1], [1,1], [1,2,1]]

for i in range(3,1001):
    new = [0] * (i+1)
    first = [0] + dp[i-1]
    second = [0] + dp[i-2] + [0]
    third = [0] + dp[i-3] + [0,0]
    for j in range(i+1):
        cur = first[j] + second[j] + third[j]
        new[j] = cur
    dp.append(new)

T = int(input())
for _ in range(T): 
    n,m = map(int, input().split())
    print(sum(dp[n-1][:m]) % 1000000009)