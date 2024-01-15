import sys 

n = int(sys.stdin.readline().rstrip())
cnt = 1
zero_cnt = 1

if n == 1 or n == 2:
    cnt = 1
else:
    # n == 4
    for i in range(n-2):
        earlier_cnt = cnt
        earlier_zero_cnt = zero_cnt
        zero_cnt = earlier_cnt
        cnt += earlier_zero_cnt
    # i == 0 / ec == 1 / ezc == 1 / zc == 1 / cnt == 2
    # i == 1 / ec == 2 / ezc == 1 / zc == 2 / cnt == 3

print(cnt)