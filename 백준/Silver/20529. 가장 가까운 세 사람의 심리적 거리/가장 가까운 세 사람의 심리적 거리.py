import sys 
input = sys.stdin.readline

def cnt_diff(string1, string2):
    return sum(char1 != char2 for char1, char2 in zip(string1, string2))

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    mbtis = [i for i in input().rstrip().split()]
    if n > 32:
        print(0)
        continue
    distances = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                dist = cnt_diff(mbtis[i], mbtis[j]) + cnt_diff(mbtis[j], mbtis[k]) + cnt_diff(mbtis[k], mbtis[i])
                distances.append(dist)
    print(min(distances))