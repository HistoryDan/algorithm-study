n = int(input())

given = n
# 주어진 수의 오른쪽 자리수
rightmost = given % 10
# 주어진 수의 각 자리 숫자의 합의 오른쪽 자리수
leftmost = (given % 10 + given // 10) % 10
# 새로운 수 
given = rightmost * 10 + leftmost
cnt = 1

while given != n:
  rightmost = given % 10
  leftmost = (given % 10 + given // 10) % 10
  given = rightmost * 10 + leftmost
  cnt += 1

print(cnt)