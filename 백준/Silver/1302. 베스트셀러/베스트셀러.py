import sys
n = int(sys.stdin.readline())
sales = {}

for _ in range(n):
    book = sys.stdin.readline().rstrip()
    if book not in sales.keys(): 
        sales[book] = 1
    else:
        sales[book] += 1

max = 0
answer = 'z'*50
for sale in sales.keys():
    current = sales[sale]
    if current > max :
        max = current
        answer = sale
    elif current == max and sale < answer:
        answer = sale

print(answer)
