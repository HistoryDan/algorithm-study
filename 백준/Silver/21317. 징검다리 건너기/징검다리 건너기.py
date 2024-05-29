import sys
input = sys.stdin.readline

n = int(input())
stone = [(0,0)]
dp = [sys.maxsize] * (n + 1)


for _ in range(n-1):
    a,b = map(int,input().split())
    stone.append((a,b))
k = int(input())

if n <= 3:
    if n == 1:
        print(0)
    elif n == 2:
        print(stone[1][0])
    else:
        print(min(stone[1][0]+stone[2][0],stone[1][1]))
else:
    dp[0] = 0
    dp[1] = 0
    dp[2] = stone[1][0]
    dp[3] = min(stone[1][0] + stone[2][0], stone[1][1])

    for i in range(4,n+1):
        dp[i] = min(stone[i-1][0]+dp[i-1], stone[i-2][1]+dp[i-2])
    result = dp[-1]
    dp2 = dp[:]

    for i in range(1,n-2):
        if dp[i]+k < dp[i+3]:
            dp2[i+3] = dp[i]+k
            for j in range(i+4,n+1):
                dp2[j] = min(dp[j], dp2[j-1]+stone[j-1][0], dp2[j-2]+stone[j-2][1])

            result = min(dp2[-1],result)
    print(result)