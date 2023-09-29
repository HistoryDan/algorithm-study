import sys
nums = [i for i in range(1,10000)]

for n in range(1,10000):
  d = n
  while n != 0:
    d += n % 10
    n //= 10
  if d >= 10000 or d < 1:
    continue
  nums[d-1] = 0

for num in nums:
  if num != 0:
    print(num)