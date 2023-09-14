numbers = input().split()
cnt_same = numbers.count(numbers[0])

if cnt_same == 3:
    print(10000 + int(numbers[0]) * 1000)
elif cnt_same == 2:
    print(1000 + int(numbers[0]) * 100)
else:
    cnt_same = numbers.count(numbers[1])
    if cnt_same == 2:
        print(1000 + int(numbers[1]) * 100)
    else:
        print(100 * max(map(int, numbers)))
