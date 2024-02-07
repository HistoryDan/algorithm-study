import sys 

n = int(sys.stdin.readline().rstrip())
scores = []
for _ in range(n):
    score = int(sys.stdin.readline().rstrip())
    scores.append(score)
if n == 1:
    print(scores[0])
else:
    dp = [[scores[0], 0], [scores[1], scores[0]+scores[1]]]
    # dp[k][0] = max(dp[k-2][0], dp[k-2][1]) + scores[k]
    # dp[k][1] = dp[k-1][0] + scores[k]

    for i in range(2,n):
        first = max(dp[i-2][0], dp[i-2][1]) + scores[i]
        second = dp[i-1][0] + scores[i]
        dp.append([first, second])

    # print(dp)
    print(max(dp[n-1]))