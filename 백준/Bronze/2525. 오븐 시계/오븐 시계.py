# 현재 시각
a,b = map(int, input().split())
# 요리 시간
cook_time = int(input())

if cook_time+b >= 60:
  print((a + ((cook_time+b) // 60)) % 24, (cook_time+b) % 60)
else:
  print(a, b+cook_time)