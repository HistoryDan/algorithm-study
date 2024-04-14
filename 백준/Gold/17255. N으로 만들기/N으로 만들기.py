import sys

cnt = 0
def foo(num):
    if len(num) == 2:
        global cnt
        front = num[0]
        rear = num[1]
        if front == rear: 
            cnt += 1
            return
        else: 
            cnt += 2
            return

    elif len(num) > 2:
        front = num[:-1]
        rear = num[1:]
        if front == rear:
            foo(front)
        else:
            foo(front)
            foo(rear)
    else:
        cnt +=1
        return 
    
N = int(input())
foo(str(N))
print(cnt)