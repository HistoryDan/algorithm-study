import sys 

while True:
    t = int(sys.stdin.readline().rstrip())
    if t == 0: break
    profits = []
    for _ in range(t):
        profit = int(sys.stdin.readline().rstrip())
        profits.append(profit)
    # D[i] := i번째 인덱스를 오른쪽 끝으로 가지는 구간의 최대합
    # D[k] := max(0, D[k-1]) + arr[k] (k > 0) , arr[k] (k == 0)
    
    dp = [profits[0]]
    for i in range(1,t):
        next = max(0, dp[i-1]) + profits[i]
        dp.append(next)

    print(max(dp))