import sys 
num = sys.stdin.readline().rstrip()
cnt = 0

while len(num) >= 2:
    sum=0
    for i in range(len(num)):
        sum += int(num[i])
    num = str(sum)
    cnt += 1

print(cnt)
if int(num)%3 == 0:
    print('YES')
else:
    print('NO')