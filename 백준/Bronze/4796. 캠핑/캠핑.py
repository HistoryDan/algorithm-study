import sys

cnt = 1
while True:
    l,p,v = map(int, sys.stdin.readline().rstrip().split())
    if l == 0 and p == 0 and v == 0 : break
    used = (v // p) * l
    rem = v % p
    if rem > l : rem = l
    used += rem
    print('Case ' + str(cnt) + ': ' + str(used))
    cnt += 1