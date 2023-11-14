import sys 
answer = 1
nums = list(map(int, sys.stdin.readline().split()))

while True:
    cnt = 0
    for num in nums:
        if answer % num == 0:
            cnt += 1
    if cnt >= 3:
        break
    answer+=1

print(answer)
