import sys 

while True:
    a,b = map(int, sys.stdin.readline().rstrip().split())
    if a==0 and b==0:
        break
    fib = [1,2]
    i = 2
    cnt = new = 0
    while new <= b:
        new = fib[i-1] + fib[i-2]
        fib.append(new)
        i += 1
    for f in fib:
        if f >= a and f <= b:
            cnt += 1

    print(cnt)