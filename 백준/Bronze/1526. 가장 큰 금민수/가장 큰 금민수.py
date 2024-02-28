import sys 

n = int(input())
digits = ['0', '1', '2', '3', '5', '6', '8', '9']

for i in range(n,0,-1):
    flag = True
    for digit in digits:
        if digit in str(i):
            flag = False
            break
    if flag:
        print(i)
        break