import sys 

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    fn = int(sys.stdin.readline().rstrip())
    fib = [0,1]
    idx = 2
    if fn == 0: print(0)
    elif fn == 1: print(2)
    else: 
        while fib[-1] != fn:
            new = fib[idx-1] + fib[idx-2]
            fib.append(new)
            idx += 1
        print(len(fib)-1)