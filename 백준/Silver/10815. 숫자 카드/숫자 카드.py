n = int(input())
n_nums = set(input().split())
m = int(input())
m_nums = input().split()
answers = []

for i in range(m):
  if m_nums[i] in n_nums:
    answers.append(1)
  else:
    answers.append(0)

print(*answers)
  