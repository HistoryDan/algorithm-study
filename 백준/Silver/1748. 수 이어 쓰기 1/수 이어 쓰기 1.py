import sys 

n = int(sys.stdin.readline().rstrip())
cur_len = len(str(n))
cnt = 0

if len(str(n)) == 1:
    print(n)

else:
    cnt += len(str(n)) * (n - int('9' * (len(str(n)) - 1)))
    n = int('9' * (len(str(n)) - 1))
    
    while n > 9 :
        cnt += len(str(n)) * 9 * 10 ** (len(str(n)) - 1)
        n = int('9'*(len(str(n))-1))

    cnt += n

    print(cnt)