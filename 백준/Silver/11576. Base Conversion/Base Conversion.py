import sys
a,b = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
a_nums = list(map(int, sys.stdin.readline().split()))

total_a = 0
for i in range(n):
    total_a +=((a ** (n-i-1)) * a_nums[i])

answers = []
while total_a != 0:
    answers.append(total_a%b)
    total_a //= b

answers = answers[::-1]
print(*answers)
    