num = int(input())
rem = []

while num != 0:
  rem.append(num % 10)
  num //= 10

rem = sorted(rem, reverse = True)
print(''.join([str(r) for r in rem]))
  