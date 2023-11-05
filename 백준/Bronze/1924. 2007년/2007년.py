import sys 
x,y = map(int, sys.stdin.readline().rstrip().split())
x_ref = [1, 3, 5, 7, 8, 10, 12]
days = 0

for i in range(1, x):

    if i == 2:
        days += 28
    elif i in x_ref:
        days += 31
    else:
        days += 30

days += y
rem = days % 7

if rem == 1: print('MON')
if rem == 2: print('TUE')
if rem == 3: print('WED')
if rem == 4: print('THU')
if rem == 5: print('FRI')
if rem == 6: print('SAT')
if rem == 0: print('SUN')

    