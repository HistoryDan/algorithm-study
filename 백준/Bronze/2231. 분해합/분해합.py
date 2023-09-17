n = int(input())
m = 0

for i in range(1,n):
  total = i
  i = str(i)
  for j in range(len(i)):
    total += int(i[j])
  if total == n:
    m = i
    break

print(m)
    
  
  
