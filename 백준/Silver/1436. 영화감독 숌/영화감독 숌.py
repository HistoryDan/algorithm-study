idx = int(input())
end = 99999999999999999999999
cnt = 0

for i in range(end):
  if '666' in str(i):
    cnt += 1
    if cnt == idx:
      print(str(i))
      break
      