import sys

iter = int(input())
numbers = [int(i) for i in input().split()]
answer = 0

for number in numbers:
  cnt = 0
  if number == 1:
    continue
  for i in range(2,number):
    if number % i == 0:
      cnt += 1
  if cnt == 0:
    answer += 1

print(answer)
