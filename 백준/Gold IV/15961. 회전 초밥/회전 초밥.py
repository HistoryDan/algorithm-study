import sys 
from collections import deque
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
foods = [int(input()) for _ in range(n)]
foods += foods[:k-1]
table = deque(foods[:k])
sushi = [0] * (d+1)
for t in table:
    sushi[t] += 1

cnt = len(set(table))
cnts = []
c_flag = True
if sushi[c] == 0:
    cnt += 1
    cnts.append(cnt)
    cnt -= 1
else:
    cnts.append(cnt)

for food in foods[k:]:
    old = table.popleft()
    sushi[old] -= 1
    if sushi[old] == 0:
        cnt -= 1
    if sushi[food] == 0:
        cnt += 1
    table.append(food)
    sushi[food] += 1
    if sushi[c] == 0:
        cnt += 1
        cnts.append(cnt)
        cnt -= 1
    else:
        cnts.append(cnt)

print(max(cnts))