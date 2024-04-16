import sys 

A,B = map(int, input().split())
cnt = 1
flag = False

while B > A:
    if B % 2 == 0:
        B //= 2
    elif B % 10 == 1:
        B -= 1
        B //= 10
    else:
        break
    cnt += 1
    if A == B:
        flag = True
        break

if flag:
    print(cnt)
else:
    print(-1)