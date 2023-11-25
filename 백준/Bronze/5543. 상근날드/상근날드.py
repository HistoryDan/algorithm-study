import sys
burgers = []
beverages = []
for _ in range(3):
    burger = int(sys.stdin.readline())
    burgers.append(burger)
for _ in range(2):
    beverage = int(sys.stdin.readline())
    beverages.append(beverage)

print(min(burgers)+min(beverages)-50)