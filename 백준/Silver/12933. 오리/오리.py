from collections import deque

string = [i for i in input().rstrip()]
answer = 0
cur = 0

while string != [0]*len(string):
    flag = False
    for i, s in enumerate(string):
        if s == 'q' and cur == 0:
            flag = False
            string[i]=0
            cur = 'q'
        elif s =='u' and cur == 'q':
            string[i]=0
            cur = 'u'
        elif s =='a' and cur == 'u':
            string[i]=0
            cur = 'a'
        elif s =='c' and cur == 'a':
            string[i]=0
            cur = 'c'
        elif s =='k' and cur == 'c':
            flag = True
            string[i]=0
            cur = 0
            
    if not flag:
        print(-1)
        break
    answer += 1

if flag:
    print(answer)