import sys

m = int(input())
first = 1
for _ in range(m):
    x,y = map(int, input().split())
    if x == first and y != first:
        first = y
    elif x != first and y == first:
        first = x

print(first)