import sys
n = int(sys.stdin.readline().rstrip())
cnt = 0
for i in range(1,n+1):
    digits = []
    while i != 0:
        digit = i % 10 
        digits.append(digit)
        i //= 10
    if len(digits) == 1:
        cnt +=1
        continue
    diff = digits[1] - digits[0]
    isSame = True
    for i in range(2, len(digits)):
        if (digits[i] - digits[i-1]) != diff:
            isSame = False
            break
    if isSame:
        cnt += 1

print(cnt)

