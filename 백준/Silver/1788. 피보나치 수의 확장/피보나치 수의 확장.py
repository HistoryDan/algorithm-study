import sys
n = int(sys.stdin.readline().rstrip())
fib = [0,1]

for i in range(2, abs(n)+1):
    new = (fib[i-1] + fib[i-2]) % 1000000000
    fib.append(new)


if n == 0:
    print(0)
elif n < 0 and n % 2 == 0:
    print(-1)
else:
    print(1)

print(fib[abs(n)])