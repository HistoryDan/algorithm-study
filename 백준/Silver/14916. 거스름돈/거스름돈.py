import sys 
money = int(sys.stdin.readline())

five = money // 5
coins = 0
isPossible = False

for i in range(five,-1,-1):
    if (money - (i*5))%2==0:
        two = (money-(i*5))//2
        coins = two+i
        isPossible = True
        break

if isPossible:
    print(coins)
else:
    print(-1)
    