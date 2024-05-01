import sys
input = sys.stdin.readline

dp = [[['1']], [['1','1'], ['2']], [['1','1','1'], ['1','2'], ['2','1'], ['3']]]

for i in range(3,12):
    new = []
    for element in dp[i-1]:
        new_element = ['1'] + element
        new.append(new_element)

    for element in dp[i-2]:
        new_element = ['2'] + element
        new.append(new_element)

    for element in dp[i-3]:
        new_element = ['3'] + element 
        new.append(new_element)

    dp.append(new)
    
N, K = map(int, input().split())
if 0 < K <= len(dp[N-1]):
    print('+'.join(dp[N-1][K-1]))
else:
    print(-1)