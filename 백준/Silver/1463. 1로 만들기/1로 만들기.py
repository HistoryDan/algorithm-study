import sys 

dp = [0,0,1,1] # n = 2, n = 3
n = int(sys.stdin.readline().rstrip())

for i in range(4,n+1):
    temp1 = temp2 = temp3 = sys.maxsize
    if i % 2 == 0:
        temp1 = dp[i//2]+1
    if i % 3 == 0:
        temp2 = dp[i//3]+1
    temp3 = dp[i-1]+1
    dp.append(min(temp1, temp2, temp3))

print(dp[n])