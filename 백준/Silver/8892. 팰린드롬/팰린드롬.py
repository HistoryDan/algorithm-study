import sys 
n = int(sys.stdin.readline())
for _ in range(n):
    m = int(sys.stdin.readline())
    words = [0 for _ in range(m)]
    found = False
    for i in range(m):
        word = sys.stdin.readline().rstrip()
        words[i] = word
    for i in range(m):
        for j in range(m):
            if i == j :
                continue
            else:
                check = words[i]+words[j]
                if check == check[::-1]:
                    found = True
                    print(check)
                    break
        if found:
            break
    if not found:
        print(0)
                    
