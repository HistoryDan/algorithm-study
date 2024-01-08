import sys 

while True:
    try:
        n = int(sys.stdin.readline().rstrip())
        digit = 1

        while True:
            if int(digit * '1') % n == 0:
                break
            digit += 1
        print(digit)
    except Exception as e:
        break