a,b = map(int, input().split())

if b >= 45:
    print(a,b-45)
elif a-1 < 0:
    print(23, 60 - (45-b))
else:
    print(a-1, 60 - (45-b))