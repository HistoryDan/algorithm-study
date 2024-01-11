import sys 

string = sys.stdin.readline().rstrip()
answer = [0 for _ in range(len(string))]
front = 0
rear = len(answer) - 1
odd_cnt = 0
flag = True

for i in range(65,91):
    char = chr(i)
    count = string.count(char)
    if count % 2 == 0:
        for _ in range(count // 2):
            answer[front] = chr(i)
            answer[rear] = chr(i)
            front += 1
            rear -= 1
    else:
        odd_cnt += 1
        if odd_cnt > 1 :
            flag = False
            break
        else:
            answer[len(answer)//2] = chr(i)
            count -= 1
            for _ in range(count//2):
                answer[front] = chr(i)
                answer[rear] = chr(i)
                front += 1
                rear -= 1

if flag:
    print(''.join(answer))
else:
    print("I'm Sorry Hansoo")