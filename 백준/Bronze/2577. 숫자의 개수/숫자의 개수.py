import sys
A = int(sys.stdin.readline().rstrip())
B = int(sys.stdin.readline().rstrip())
C = int(sys.stdin.readline().rstrip())
digits = [0 for _ in range(10)]
mul = A * B * C

while mul != 0:
  rem = mul % 10
  for i in range(10):
    if rem == i:
      digits[rem] += 1
  mul //= 10

for digit in digits:
  print(digit)