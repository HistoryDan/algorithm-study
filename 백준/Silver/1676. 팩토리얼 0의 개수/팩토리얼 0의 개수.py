n = int(input())
cnt_t = 0
cnt_f = 0

for j in range(2,n+1):
  while j % 2 == 0:
    j //= 2
    cnt_t += 1
  
  while j % 5 == 0:
    j //= 5
    cnt_f += 1
  
print(min(cnt_t, cnt_f))
