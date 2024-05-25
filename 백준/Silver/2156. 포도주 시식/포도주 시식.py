import sys
input = sys.stdin.readline

N = int(input())
array = [int(input()) for _ in range(N)]
dp = [0] * N
dp[0] = array[0]

if N > 1:
    dp[1] = array[0]+array[1]

if N > 2: 
    dp[2] = max(array[0]+array[2], array[1]+array[2], array[0]+array[1])

if N > 3: 
    for i in range(3,N):
        second = array[i] + dp[i-2]
        third = array[i] + array[i-1] + dp[i-3]
        dp[i] = max(dp[i-1], second, third)


answer = 0
for j in range(N):
    if dp[j] > answer:
        answer = dp[j]

print(answer)