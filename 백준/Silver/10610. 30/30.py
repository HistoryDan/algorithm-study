import sys
n = int(sys.stdin.readline())
digits = []

while n != 0:
    digit = n%10
    digits.append(digit)
    n //= 10

if (0 in digits) and (sum(digits)%3==0):
    digits = sorted(digits, reverse = True)
    for digit in digits:
        print(digit, end='')
else:
    print(-1)
