import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
m1 = []
m2 = []
cnt = 0
successed = False

def change(A, p, q):
  B = A
  for i in range(3):
    for j in range(3):
      if B[p+i][q+j] == 0:
        B[p+i][q+j] = 1
      else:
        B[p+i][q+j] =0
  return B
  
for _ in range(n):
  row = sys.stdin.readline().rstrip()
  m1.append([int(row[i]) for i in range(m)])

for _ in range(n):
  row = sys.stdin.readline().rstrip()
  m2.append([int(row[i]) for i in range(m)])

# for i in range(n-2):
#   if m1 == m2:
#     successed = True
#     break
#   for j in range(m-2):
#     if m1[i][j] != m2[i][j]:
#       m1 = change(m1,i,j)
#       cnt += 1
#       if m1 == m2:
#         successed = True
#         break

for i in range(n):
    for j in range(m):
        if i < n - 2 and j < m - 2 and m1[i][j] != m2[i][j]:
            m1 = change(m1, i, j)
            cnt += 1

# 최종적으로 m1과 m2를 비교하여 성공 여부 확인
if m1 == m2:
    successed = True


if successed:
  print(cnt)
else:
  print(-1)