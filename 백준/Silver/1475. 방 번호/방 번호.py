import sys
import math

number = int(sys.stdin.readline().rstrip())
digits = []
counts = [0 for _ in range(9)]

while number != 0:
    digit = number % 10
    digits.append(digit)
    number //= 10

for digit in digits:
    if digit == 9:
        counts[5] += 1
    else:
        counts[digit-1] += 1

counts[5] = math.ceil(counts[5]/2)

print(max(counts))