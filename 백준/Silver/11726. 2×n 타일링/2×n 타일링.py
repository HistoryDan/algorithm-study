n = int(input())
r = 0
answer = 1

while n-r > r:
    r += 1
    top = 1
    bottom = 1
    for i in range(1,r+1):
        top *= (n-r+1-i)
        bottom *= i
    answer += int(top//bottom)

print(answer%10007)