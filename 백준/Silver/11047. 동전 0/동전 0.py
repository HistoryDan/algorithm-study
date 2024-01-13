import sys
n,k = map(int, sys.stdin.readline().rstrip().split())
coins = []
cnt = 0

for _ in range(n):
    coin = int(sys.stdin.readline())
    coins.append(coin)

coins = coins[::-1]
for coin in coins:
    if k == 0:
        break
    elif coin > k:
        continue
    else:
        cnt += (k//coin)
        k %= coin
           
print(cnt)
