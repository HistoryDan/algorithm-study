import sys 
s = int(sys.stdin.readline())
i = 1
while (i*(i+1))//2 < s:
    i += 1

if (i*(i+1))//2 == s:
    print(i)
else:
    print(i-1)