import sys

money = int(sys.stdin.readline().rstrip())
a = int(money * 0.78)
b = int(money  - (money * 0.2 * 0.22))

print(a, b)