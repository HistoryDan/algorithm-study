import sys 
input = sys.stdin.readline

dp = [(1,0), (1,1), (2,2)] # 타일 홀수개, 타일 짝수개 쓰는 경우의 수
for i in range(3, 100001):
    odd_num = dp[i-1][1] + dp[i-2][1] + dp[i-3][1]
    even_num = dp[i-1][0] + dp[i-2][0] + dp[i-3][0]
    dp.append((odd_num % 1000000009, even_num % 1000000009))

T = int(input())
for _ in range(T):
    n = int(input())
    odd, even = dp[n-1]
    print(odd , even)